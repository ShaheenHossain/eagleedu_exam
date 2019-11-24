# -*- coding: utf-8 -*-
{
    'name': "Eagle Education Exam Module",
    'summary': """ This is a Eagle Education Exam Module""",
    'description': """ This is a Eagle Education Exam Module """,
    'author': "Eagle ERP",
    'website': "http://www.eagle-erp.com",
    'category': 'Education',
    'version': '0.1',

    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        'views/eagleedu_exam.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}