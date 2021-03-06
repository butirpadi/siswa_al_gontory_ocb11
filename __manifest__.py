# -*- coding: utf-8 -*-
{
    'name': "Siswa PAUD for TK Al Gontori",

    'summary': """
        Integrate module for Siswa Module only for PAUD Level on TK Al Gontori""",

    'description': """
        Integrate module for Siswa Module only for PAUD Level on TK Al Gontori
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'siswa_ocb11', 'siswa_keu_ocb11', 'siswa_tab_ocb11', 'siswa_psb_ocb11'],

    # always loaded
    'data': [
        'data/ir_model_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}