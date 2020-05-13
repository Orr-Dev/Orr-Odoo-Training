# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "IPPay Payment Acquirer for Credit Cards",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "summary": "Store and use credit cards using IPPay",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "maintainer": "Open Source Integrators",
    "website": "http://www.opensourceintegrators.com",
    "category": "Accounting",
    "depends": ["payment", "website", "account_payment"],
    "data": [
        "views/payment_view.xml",
        "views/payment_ippay_templates.xml",
        "data/ippay_payment_data.xml",
        "data/account_payment_method.xml",
        "views/account_portal_templates.xml",
    ],
    "development_status": "beta",
    "installable": True,
    "external_dependencies": {"python": ["xmltodict"]},
}