# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Stock',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base Stock Customization',
    'description': """
        * This module extends Odoo enterprise edition modules. So enterprise addons is required.
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
        'stock',
        'fleet',
        'aq_storer'
        ],
    'data': [
        'data/readonly_group_data.xml',
        'security/ir.model.access.csv',
        'views/templates/stock_report_picking.xml',
        'views/stock_move_line.xml',
        'views/stock_menu_items.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
