# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Product',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base product Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base','product','website_sale_stock', 'purchase', 'sale'],
    'data': [
        'views/product.xml',
        'views/sale.xml',
        'views/product_pricelist.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
