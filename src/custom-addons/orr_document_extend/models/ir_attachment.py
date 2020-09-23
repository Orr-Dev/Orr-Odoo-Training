from odoo import models, fields,api


class IrAttachment(models.Model) :
    _inherit = "ir.attachment"
    
    @api.model
    def default_get(self, fields):

         res = super(IrAttachment, self).default_get(fields)
         #check for active id
         active_id = self._context.get('active_id')
         if self.env.context.get('active_model') == 'project.project' and active_id:
             #get active project 
             active_project = self.env['project.project'].browse(active_id)
             #get active customer    
             active_customer = active_project.partner_id
             #assign partner_id in return dictionary
             res['partner_id'] = active_customer.id
         
         return res
