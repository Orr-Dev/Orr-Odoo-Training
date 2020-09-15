from odoo import api,fields, models

class Partners(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        orig_res = super().name_get()
        # orig_names = {rec_id: rec_name for rec_id, rec_name in orig_res}
        orig_names = dict(orig_res)  # even simpler
        res = []
        for record in self:
            # naive, ignores super():
            name = record.name
            # optimized, uses super():
            name = orig_names[record.id]
            city = record.city
            state = record.state_id.name
            display_name = "%s (%s, %s)" % (name, city, state)
            res.append((record.id, display_name))
        return res