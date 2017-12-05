# -*- coding: utf-8 -*-

from odoo import models, fields, api


class service(models.Model):
     _name = 'la_costera.service'

     id = fields.Char(integer="ID", required=True)
     vehicle = fields.Char(string="Vehicle", required=True)
     action= fields.Char(string="Action", required=True)
     startdate = fields.Datetime(string="Start Date", required=False)
     finishdate = fields.Datetime(string="Finish Date", required=False)

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
