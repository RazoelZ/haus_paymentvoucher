{
    'name': 'Haus Payment Voucher',
    'version': '1.0',
    'summary': 'Haus Payment Voucher',
    'sequence': -9,
    'description': """Haus Payment Voucher""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'board',
        'dev_employee_master_data',
        'web_digital_sign',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/paymentvoucher.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dev_crm_haus/static/**/*',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
