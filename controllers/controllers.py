# -*- coding: utf-8 -*-
from odoo import http

# class Acrossing(http.Controller):
#     @http.route('/acrossing/acrossing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acrossing/acrossing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('acrossing.listing', {
#             'root': '/acrossing/acrossing',
#             'objects': http.request.env['acrossing.acrossing'].search([]),
#         })

#     @http.route('/acrossing/acrossing/objects/<model("acrossing.acrossing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acrossing.object', {
#             'object': obj
#         })