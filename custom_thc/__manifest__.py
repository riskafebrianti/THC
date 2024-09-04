# -*- coding: utf-8 -*-
{
    'name': "custom_thc",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base','sale',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/barcode.xml',
        'views/templates.xml',
        'report/templet_boxed.xml',
        'report/sd.xml',
        'report/fu.xml',
        'report/invTHC.xml',
        # 'report/sale_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
