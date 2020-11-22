# -*- coding: utf-8 -*-
# from odoo import http


# class TodorocApp(http.Controller):
#     @http.route('/todoroc_app/todoroc_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todoroc_app/todoroc_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todoroc_app.listing', {
#             'root': '/todoroc_app/todoroc_app',
#             'objects': http.request.env['todoroc_app.todoroc_app'].search([]),
#         })

#     @http.route('/todoroc_app/todoroc_app/objects/<model("todoroc_app.todoroc_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todoroc_app.object', {
#             'object': obj
#         })
