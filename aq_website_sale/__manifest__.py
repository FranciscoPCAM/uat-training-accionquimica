# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Website sale',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base website sale',
    'description': """
        * Add new required functionalities to website sale module (Ecommerce).
    """,
    'website': 'https://www.portcities.net',
    'author':'Port Cities Ltd.',
    'depends': ['base','website_sale'],
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
