# -*- coding: utf-8 -*-

from odoo import models, fields, api

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class client(models.Model):
     _name = 'la_costera.client'

     id = fields.Char(integer="ID", required=True)
     tin = fields.Char(string="TIN", required=True)
     name= fields.Char(string="Name", required=True)
     surname = fields.Char(string="Surname", required=True)
     telephone = fields.Char(integer="Telephone Nº", required=True)
     type = fields.Boolean(string ="Client type", required=True)

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
