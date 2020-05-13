# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'OSI ACH-Batch Discount Connector',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'Open Source Integrators',
    'category': 'Accounting',
    'maintainer': 'Open Source Integrators',
    'website': 'http://www.opensourceintegrators.com',
    'maintainers': ['bodedra'],
    'depends': [
        'osi_custom_payment_term',
        'osi_payment_batch_process',
        'account_payment_order',
        'account_banking_ach_credit_transfer',
        'account_banking_ach_direct_debit',
    ],
    'data': [
       'views/account_payment_view.xml',
    ],
    'installable': True,
}