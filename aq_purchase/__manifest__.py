# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AQ - Purchase',
    'version': '15.0.1.0.0',
    'category': '',
    'summary': 'Odoo base purchase Customization',
    'description': """
        * Add new required fields and functionalities.
    """,
    'website': 'https://www.portcities.net',
    'author':'Port Cities Ltd.',
    'depends': ['base',
                'purchase',
                'aq_partner',
                'account',
                'purchase_requisition',
                'purchase_stock',
                'product',
                'stock'
                ],
    'data': [
        'data/visualizer_group_data.xml',
        'security/ir.model.access.csv',
        'views/purchase.xml',
        'views/partner.xml',
        'views/vendor_rank.xml',
        'views/product.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
