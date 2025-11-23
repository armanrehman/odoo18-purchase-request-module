{
    'name': 'Purchase Request',
    'version': '18.0.1.0',
    'summary': 'Purchase Request functionality for the Purchase module',
    'author': 'Arman Rehman',
    'license': 'LGPL-3',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/purchase_request_sequence.xml',
        'views/purchase_request_views.xml',
        'reports/purchase_request_report.xml',
    ],
    'installable': True,
    'application': True
}