# -*- coding: utf-8 -*-
from odoo import http

# class LaCostera(http.Controller):
#     @http.route('/la_costera/la_costera/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/la_costera/la_costera/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('la_costera.listing', {
#             'root': '/la_costera/la_costera',
#             'objects': http.request.env['la_costera.la_costera'].search([]),
#         })

#     @http.route('/la_costera/la_costera/objects/<model("la_costera.la_costera"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('la_costera.object', {
#             'object': obj
#         })