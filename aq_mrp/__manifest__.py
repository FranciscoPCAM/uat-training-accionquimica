# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - MRP',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base MRP Customization',
    'description': """
        * This module extends Odoo enterprise edition modules. So enterprise addons is required.
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
        'mrp'
        ],
    'data': [
        'views/mrp_production_form_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
