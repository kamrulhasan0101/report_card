# -*- coding: utf-8 -*-

from odoo import api, models


class ParticularReport(models.AbstractModel):
    _name = 'report.report_card.dis_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(docids[0])
        docs = self.env['exam.result'].browse(docids[0])
        add_result = self.env['additional.exam.result'].search([('student_id',
                                                                 '=', 4)])
        if add_result is None:
            vals = {
                'a_exam': "test_exam",
                'subject': "test_sub",
                'marks': "test_mark",
                'roll': "test_roll"
            }

        else:
            for a_r in add_result:
                vals = {
                    'a_exam': a_r.a_exam_id,
                    'marks': a_r.obtain_marks,
                    'roll': a_r.roll_no_id
                }
            additional_result = []
        additional_result.append(vals)
        return {
            'doc_model': 'exam.result',
            'data': data,
            'docs': docs,
            'additional_result': additional_result,
        }
