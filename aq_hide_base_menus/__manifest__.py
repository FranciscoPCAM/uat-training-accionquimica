# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Hide Odoo Menus',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Custom module for hide base odoo menus',
    'description': """
        * rewrite required menu data.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
                'mail',
                'contacts',
                'calendar',
                'website',
                'maintenance',
                'hr',
                'hr_expense',
                'quality_control',
                ],
    'data': [
        'data/mail_menu_data.xml',
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
