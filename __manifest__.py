# -*- coding: utf-8 -*-

{
    'name': 'Sale order lock with access right',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Sale',
    'description': "",
    'depends': [
        'sale'
    ],
    'data': [
        'security/sale_order_lock_with_access_right_security.xml',
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
