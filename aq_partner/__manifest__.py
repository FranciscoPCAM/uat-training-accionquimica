# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Custom Partner',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base partner Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Portcities Ltd.',
    'depends': ['base', 'account','stock','aq_product', 'aq_account_group', 'hr', 'hr_contract', 'aq_stock'],
    'data': [
        'views/partner.xml',
        'views/account_payment_term.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
