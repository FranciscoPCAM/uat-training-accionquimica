# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom CRM Lead',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base CRM Lead Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 'crm'],
    'data': [
        'views/crm_lead.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
