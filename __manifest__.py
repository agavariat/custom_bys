# -*- coding: utf-8 -*-
{
    'name': "custom_modulo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','l10n_co_res_partner','payment_report_co',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_bys.xml',
        'reports/report_delivery_inherit.xml',
        'views/stock_move_bys.xml',
        'data/record_required_process.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}