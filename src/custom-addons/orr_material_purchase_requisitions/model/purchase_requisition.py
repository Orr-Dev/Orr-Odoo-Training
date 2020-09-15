from odoo import api, fields, models

class PurchaseRequisition(models.Model):
    _inherit = 'material.purchase.requisition'

    partner_id = fields.Many2one("project_id.partner_id")