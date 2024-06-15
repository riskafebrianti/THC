# -*- coding: utf-8 -*-
# from odoo import http


# class CustomThc(http.Controller):
#     @http.route('/custom_thc/custom_thc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_thc/custom_thc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_thc.listing', {
#             'root': '/custom_thc/custom_thc',
#             'objects': http.request.env['custom_thc.custom_thc'].search([]),
#         })

#     @http.route('/custom_thc/custom_thc/objects/<model("custom_thc.custom_thc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_thc.object', {
#             'object': obj
#         })
