# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tarefa(models.Model):
    _name = 'tarefa.tarefa'
    _description = 'tarefa.tarefa'

    name = fields.Char(string="Nome", required=True)
    done = fields.Boolean(string="Concluída")

    partner_id = fields.Many2one('res.partner', ondelete='restrict', string="Responsável")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
