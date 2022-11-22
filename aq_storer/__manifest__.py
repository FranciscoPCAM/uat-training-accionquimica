# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Storer user',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Custom module for Storer user functionalities',
    'description': """
        * Add new required fields, groups and processes.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
                'stock'],
    'data': [
        'data/storer_group_data.xml',
        'security/ir.model.access.csv',
        'views/stock_picking.xml',
        'views/stock_quant_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
