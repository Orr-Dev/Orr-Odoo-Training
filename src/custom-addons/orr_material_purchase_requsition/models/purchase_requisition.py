from odoo import models,fields

class Requsition(models.Model):
    _inherit = "material.purchase.requisition"
    partner_id = fields.Many2one(
        'res.partner', 
        string = 'Customer',
        )
    