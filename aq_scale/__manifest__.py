# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Scale',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Scale Custom module',
    'description': """
        * This module extends Odoo enterprise edition modules. So enterprise addons is required.
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
        'stock'
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking.xml',
        'views/scale_weight.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
