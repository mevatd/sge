# -*- coding: utf-8 -*-

from odoo import models, fields, api

class action(models.Model):
     _name = 'la_costera.action'

     id = fields.Char(string="ID", required=True)
     name = fields.Char(string="Name", required=True)
     cost = fields.Float(string="Cost", required=True)
     startdate = fields.Datetime(string="Start Date", required=False)
     finishdate = fields.Datetime(string="Finish Date", required=False)
     worker = fields.Many2one('la_costera.worker', 'Worker')
     product = fields.Many2one('la_costera.product', 'Product')

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
