# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Account',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base Account Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base','account','account_asset','payment'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_asset.xml',
        'views/banamex_currency.xml',
        'views/account_move.xml',
        'views/purchase_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
