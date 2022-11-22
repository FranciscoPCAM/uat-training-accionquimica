# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Account Access Group',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base Account Access Customization',
    'description': """
        * Add new required access groups.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base','account','aq_account','account_accountant'],
    'data': [
        'data/conciliation_group_data.xml',
        'security/ir.model.access.csv',
        'views/banamex_currency.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
