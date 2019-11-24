# -*- coding: utf-8 -*-
from eagle import http

# class EagleeduExam(http.Controller):
#     @http.route('/eagleedu_exam/eagleedu_exam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eagleedu_exam/eagleedu_exam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eagleedu_exam.listing', {
#             'root': '/eagleedu_exam/eagleedu_exam',
#             'objects': http.request.env['eagleedu_exam.eagleedu_exam'].search([]),
#         })

#     @http.route('/eagleedu_exam/eagleedu_exam/objects/<model("eagleedu_exam.eagleedu_exam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eagleedu_exam.object', {
#             'object': obj
#         })