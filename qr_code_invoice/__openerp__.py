# -*- coding: utf-8 -*-
{
    'name': 'QR Code Invoice',
    'version': '8.0.1.0.0',
    'category': 'Accounting',
    'author': 'ERP Harbor Modification v8',
    'summary': 'Generate QR Code for Invoice',
    'website': 'http://www..com',
    'description': """""",
    'depends': [
        'qr_code_base',
        'account',
    ],
    'data': [
        'report/account_invoice_report_template.xml',
        'views/qr_code_invoice_view.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
}
