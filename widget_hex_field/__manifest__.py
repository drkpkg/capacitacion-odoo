# -*- coding: utf-8 -*-
{
    'name': "Widget Hex Field",

    'summary': "This module adds a new widget to the Odoo framework, which allows you to enter hexadecimal values",

    'description': """
        This module adds a new widget to the Odoo framework, which allows you to enter hexadecimal values in a field.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Web',
    'version': '17.0.1.0.0',
    'depends': ['web', 'sale_management'],
    'data': [
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'widget_hex_field/static/src/components/**/*',
        ],
    },
}

