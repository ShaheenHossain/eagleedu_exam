# -*- coding: utf-8 -*-

from eagle import models, fields, api

# class eagleedu_exam(models.Model):
#     _name = 'eagleedu_exam.eagleedu_exam'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100