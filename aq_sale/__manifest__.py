# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Sale',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base sale Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Port Cities Ltd.',
    'depends': ['base','sale','sales_team', 'aq_partner', 'website_sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/capturista_group_data.xml',
        'views/sale.xml',
        'views/company.xml',
        'views/partner.xml',
        'views/crm_lead.xml',
        'views/product.xml',
        'views/product_pricelist.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
