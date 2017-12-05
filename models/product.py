# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product(models.Model):
     _name = 'la_costera.product'

     id = fields.Char(string="ID", required=True)
     name = fields.Char(string="Name", required=True)
     cost = fields.Float(string="Cost", required=True)
     action = fields.One2many('la_costera.action', 'product')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
