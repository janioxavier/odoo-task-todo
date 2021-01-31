from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    nomeMae = fields.Char(string="Nome da mãe")