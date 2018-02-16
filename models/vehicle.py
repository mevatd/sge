# -*- coding: utf-8 -*-

from odoo import models, fields, api


class service(models.Model):
     _name = 'la_costera.vehicle'

     id = fields.Char(integer="ID", required=True)
     name = fields.Char(compute='_get_composed_name')
     licensePlateNumber = fields.Char(string="License Plate Number", required=True)
     vin = fields.Char(string="VIN", required=True)
     brand = fields.Char(string="Brand", required=True)
     model = fields.Char(string="Model", required=True)
     photo = fields.Binary()
     service = fields.One2many('la_costera.service', 'vehicle')
     client = fields.Many2one('la_costera.client', 'Client')

     @api.depends('brand', 'model', 'licensePlateNumber')
     def _get_composed_name(self):
         for s in self:
             s.name = s.brand + "," + s.model + "," + s.licensePlateNumber
