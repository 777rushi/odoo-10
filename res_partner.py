from openerp import api, fields, models, _

class res_partner(models.Model):
    _inherit = "res.partner"

    external_id = fields.Char(string="External Id")
