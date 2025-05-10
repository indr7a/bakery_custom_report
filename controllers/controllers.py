# -*- coding: utf-8 -*-
# from odoo import http


# class BakeryCustomReport(http.Controller):
#     @http.route('/bakery_custom_report/bakery_custom_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bakery_custom_report/bakery_custom_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bakery_custom_report.listing', {
#             'root': '/bakery_custom_report/bakery_custom_report',
#             'objects': http.request.env['bakery_custom_report.bakery_custom_report'].search([]),
#         })

#     @http.route('/bakery_custom_report/bakery_custom_report/objects/<model("bakery_custom_report.bakery_custom_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bakery_custom_report.object', {
#             'object': obj
#         })

