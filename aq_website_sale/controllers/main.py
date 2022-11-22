# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.urls import url_decode, url_encode, url_parse

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.fields import Command
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.payment.controllers import portal as payment_portal
from odoo.addons.payment.controllers.post_processing import PaymentPostProcessing
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.addons.website.controllers import main
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.osv import expression
from odoo.tools.json import scriptsafe as json_scriptsafe
_logger = logging.getLogger(__name__)


from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute

class CustomWebsiteSale(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super().shop(page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post)
        
        Category = request.env['product.public.category']
        attrib_list = request.httprequest.args.getlist('attrib')
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attributes_ids = {v[0] for v in attrib_values}
        filter_by_price_enabled = request.website.is_view_active('website_sale.filter_products_price')
        
        if filter_by_price_enabled:
            company_currency = request.website.company_id.currency_id
            conversion_rate = request.env['res.currency']._get_conversion_rate(company_currency, pricelist.currency_id, request.website.company_id, fields.Date.today())
        else:
            conversion_rate = 1

        if ppg:
            try:
                ppg = int(ppg)
                post['ppg'] = ppg
            except ValueError:
                ppg = False
        if not ppg:
            ppg = request.env['website'].get_current_website().shop_ppg or 20

        pricelist_context, pricelist = self._get_pricelist_context()

        options = {
            'displayDescription': True,
            'displayDetail': True,
            'displayExtraDetail': True,
            'displayExtraLink': True,
            'displayImage': True,
            'allowFuzzy': not post.get('noFuzzy'),
            'category': str(category.id) if category else None,
            'min_price': min_price / conversion_rate,
            'max_price': max_price / conversion_rate,
            'attrib_values': attrib_values,
            'display_currency': pricelist.currency_id,
        }
        product_count, details, fuzzy_search_term = request.website._search_with_fuzzy("products_only", search,
            limit=None, order=self._get_search_order(post), options=options)
        search_product = details[0].get('results', request.env['product.template']).with_context(bin_size=True)
        product_pricelist = request.env['product.pricelist.item'].search([('pricelist_id.selectable','=',True)])
        items = []
        for item in product_pricelist:
            if item.product_id.product_tmpl_id.id in search_product.ids and item.product_id.product_tmpl_id.id not in items:
                items.append(item.product_id.product_tmpl_id.id)
        search_product = request.env['product.template'].search([('id','in',items)])
        print('RENIER RENIER ERNIER RERNIENRIE')
        print(search_product)
        print(search_product)
        print(product_count)
        print(product_count)
        website_domain = request.website.website_domain()
        if search:
            search_categories = Category.search([('product_tmpl_ids', 'in', search_product.ids)] + website_domain).parents_and_self

        url = "/shop"
        if category:
            url = "/shop/category/%s" % slug(category)
        pager = request.website.pager(url=url, total=product_count, page=page, step=ppg, scope=7, url_args=post)
        offset = pager['offset']
        products = search_product[offset:offset + ppg]

        ProductAttribute = request.env['product.attribute']
        if products:
            # get all products without limit
            attributes = ProductAttribute.search([
                ('product_tmpl_ids', 'in', search_product.ids),
                ('visibility', '=', 'visible'),
            ])
        else:
            attributes = ProductAttribute.browse(attributes_ids)

        ppr = request.env['website'].get_current_website().shop_ppr or 4
        
        res.qcontext['products'] = products
        res.qcontext['bins'] = TableCompute().process(products, ppg, ppr)
        res.qcontext['attributes'] = attributes

        return res