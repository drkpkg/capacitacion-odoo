# -*- coding: utf-8 -*-
{
    'name': "Fleet Reservation",

    'summary': "Módulo para gestionar reservas de vehiculos",

    'description': """
Módulo para gestionar reservas de vehículos.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Fleet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts', 'fleet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_views.xml',
        'views/fleet_reservation_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    
    'license': 'LGPL-3',
}

