from odoo import models, fields

class IrAttachment(models.Model) :
    _inherit = "ir.attachment"

   # @api.model
    def default_get(self,default_fields):
         res = super(IrAttachment, self).default_get(default_fields)
         print(res)
         print('ActiveId:')
         print(res['active_id'])
         print('Active Model')
         print(res['active_model'])
         return res