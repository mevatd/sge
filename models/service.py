# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class service(models.Model):
     _name = 'la_costera.service'
     id = fields.Char(integer="ID", required=True)
     template = fields.Boolean(string ="Template", required=True)
     name = fields.Char(string="Name", required=True)
     vehicle = fields.Many2one('la_costera.vehicle', 'Vehicle')
     photo = fields.Binary(related='vehicle.photo', string='Photo')
     todo = fields.One2many('la_costera.todo', 'service')
     progress = fields.Float(string="Completed Actions", compute='_completed_actions')
     price = fields.Float(string="Price", compute='_overall_price')
     startdate = fields.Datetime(string="Start Date", required=False)
     finishdate = fields.Datetime(string="Finish Date", required=False)
     hiddenComputed = fields.Boolean(compute='_completed_services')
     hiddenStatic = fields.Boolean()


     @api.depends('todo')
     def _completed_actions(self):
         for s in self:
             cntTotal = 0
             cntCompl = 0
             for t in s.todo:
                 if t.finished == True:
                     cntCompl = cntCompl + 1
                 cntTotal = cntTotal + 1
             if cntTotal == 0:
                 s.progress = 0
             else:
                 s.progress = (float(cntCompl) / float(cntTotal)) * 100

     @api.depends('price')
     def _overall_price(self):
         for s in self:
            totalPrice = 0
            for t in s.todo:
                for a in t.action:
                    totalPrice = totalPrice + a.price
            s.price = totalPrice


     @api.depends('progress')
     def _completed_services(self):
        for s in self:
            if(s.progress == 100):
                s.hiddenComputed = True
                s.write({'hiddenStatic' : True})
            else:
                s.hiddenComputed = False
                s.write({'hiddenStatic' : False})

     @api.multi
     def new_tmpl_service(self):
         self.create({'name': self.name})
         self.create({'vehicle': self.vehicle.id})
         self.create({'todo': self.todo})
         self.create({'price': self.price})





#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
