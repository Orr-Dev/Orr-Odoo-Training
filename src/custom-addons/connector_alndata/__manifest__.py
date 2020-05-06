# Copyright (C) 2019 Open Source Integrators
# Copyright (C) 2019 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'ALN Data Connector',
    'summary': '''This module allows you to synchronize your Odoo database
                with ALN Data once a month''',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Open Source Integrators, Odoo Community Association (OCA),',
    'website': 'https://github.com/OCA/l10n-usa',
    'category': 'Tools',
    'maintainers': ['max3903'],
    'development_status': 'Beta',
    'depends': [
        'crm',
        'fieldservice',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter_data.xml',
        'data/sync_aln_data_view.xml',
        'views/res_partner_industry_view.xml',
        'views/res_partner_view.xml',
        'views/aln_feed_view.xml',
        'views/fsm_location.xml',
    ],
    'installable': True,
}
