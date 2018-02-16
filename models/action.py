# -*- coding: utf-8 -*-

from odoo import models, fields, api

class action(models.Model):
     _name = 'la_costera.action'

     id = fields.Char(string="ID", required=True)
     name = fields.Char(string="Name", required=True)
     cost = fields.Float(string="Cost", required=True)
     price = fields.Float(string="Price", compute='_total_price')
     startdate = fields.Datetime(string="Start Date", required=False)
     finishdate = fields.Datetime(string="Finish Date", required=False)
     worker = fields.Many2many('la_costera.worker')
     product = fields.Many2one('la_costera.product', 'Product')
     todo = fields.One2many('la_costera.todo', 'action')

     @api.depends('price')
     def _total_price(self):
         profit = 1.4
         for a in self:
            a.price = a.cost * profit
