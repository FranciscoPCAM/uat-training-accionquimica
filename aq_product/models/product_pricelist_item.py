# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'
    _description = 'Product Pricelist Item'

    def _check_product_currency(self, rec, product_id=False):
        if product_id:
            if product_id.main_currency_id.id != rec.currency_id.id:
                raise ValidationError(_("El producto seleccionado no es compatible con la moneda de la lista de precios."))
        return True


    @api.onchange('product_tmpl_id')
    def _onchange_product_tmpl_id(self):
        res = super(ProductPricelistItem, self)._onchange_product_tmpl_id()
        for line in self:
            if line.product_tmpl_id:
                line._check_product_currency(line, line.product_tmpl_id)
        return res

    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super(ProductPricelistItem, self)._onchange_product_id()
        for line in self:
            if line.product_id:
                line._check_product_currency(line, line.product_id)
        return res