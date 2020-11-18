# -*- coding: utf-8 -*-
# from odoo import http


# class ReportCard(http.Controller):
#     @http.route('/report_card/report_card/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_card/report_card/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_card.listing', {
#             'root': '/report_card/report_card',
#             'objects': http.request.env['report_card.report_card'].search([]),
#         })

#     @http.route('/report_card/report_card/objects/<model("report_card.report_card"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_card.object', {
#             'object': obj
#         })
