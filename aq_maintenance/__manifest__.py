# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Maintenance',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base Maintenance Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 'maintenance', 'delivery'],
    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_request.xml',
        'views/product_template.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
