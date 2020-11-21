# -*- coding: utf-8 -*-

from odoo import api, models


class ParticularReport(models.AbstractModel):
    _name = 'report.report_card.dis_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(docids[0])
        docs = self.env['exam.result'].browse(docids[0])
        add_result = self.env['additional.exam.result'].search([('student_id',
                                                                 '=', docids[0])])
        return {
            'doc_model': 'exam.result',
            'data': data,
            'docs': docs,
            'additional_result': add_result,
        }
