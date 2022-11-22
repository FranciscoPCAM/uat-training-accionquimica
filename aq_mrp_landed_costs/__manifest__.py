# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Landed Costs',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base Landed Costs Customization',
    'description': """
        * This module extends Odoo enterprise edition modules. So enterprise addons is required.
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
        'mrp_landed_costs', 
        'stock',
        'l10n_mx_edi_stock_extended',
        'stock_account',
        ],
    'data': [
        'views/stock_picking_type.xml',
        'views/stock_picking.xml',
        'views/stock_valuation_layer.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
