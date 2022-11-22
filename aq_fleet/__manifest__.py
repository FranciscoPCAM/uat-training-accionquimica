# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Fleet',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base Fleet Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 
                'fleet', 
                'l10n_mx_edi_stock', 
                'stock', 
                'hr_expense'],
    'data': [
        'security/ir.model.access.csv',
        'data/fleet_service_data.xml',
        'views/fleet_vehicle.xml',
        'views/stock_picking.xml',
        'views/fleet_vehicle_log_services.xml',
        'views/hr_expense.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
