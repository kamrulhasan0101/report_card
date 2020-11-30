# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class ExamSchedule(models.Model):
    _inherit = 'exam.schedule.line'

    @api.onchange('standard_id')
    def onchange_standard(self):
        '''Method to get standard according to the standard selected'''

    standard_id = fields.Many2one('standard.standard', 'standard_id')
    timetable_id = fields.Many2one('time.table', 'standard_id')
    exam_id = fields.Many2one('exam.exam', 'Exam')
    standard_ids = fields.Many2many('standard.standard',
                                    string='Participant Standards')


class ExamResultInherit(models.Model):
    _inherit = 'exam.subject'
    cq_marks = fields.Float("CQ Marks")
    mcq_marks = fields.Float("MCQ Marks")
    practical_marks = fields.Float("Practical Marks")
    total_exam_marks = fields.Float("Total", compute='_compute_total_exam_marks', store=True)
    con_total_marks = fields.Float("Con. Total", compute='_compute_con_total_exam_marks', store=True)
    obtain_marks = fields.Float("Obtain Mark", compute='_compute_obtain_marks', store=True)
    sba_marks = fields.Float("SBA")
    ct_marks = fields.Float("CT")
    marks_reeval = fields.Float("Marks After Re-evaluation",
                                help="Marks Obtain after Re-evaluation")
    highest_marks = fields.Float("Highest Marks", compute='_compute_highest_marks')
    grade_line_id = fields.Many2one('grade.line', "Grade",
                                    compute='_compute_grade')

    @api.depends('mcq_marks', 'cq_marks', 'practical_marks')
    def _compute_total_exam_marks(self):
        '''Method to compute total exam marks'''
        for rec in self:
            total_exam_marks = 0.0
            if rec.mcq_marks:
                total_exam_marks += rec.mcq_marks
            if rec.cq_marks:
                total_exam_marks += rec.cq_marks
            if rec.practical_marks:
                total_exam_marks += rec.practical_marks
            rec.total_exam_marks = total_exam_marks

    @api.depends('sba_marks', 'ct_marks', 'con_total_marks')
    def _compute_obtain_marks(self):
        '''Method to compute obtain marks'''
        for rec in self:
            additional_marks = rec.sba_marks + rec.ct_marks
            rec.obtain_marks = round(rec.con_total_marks + additional_marks)

    @api.depends('total_exam_marks')
    def _compute_con_total_exam_marks(self):
        '''Method to compute con total exam marks'''
        for rec in self:
            rec.con_total_marks = rec.total_exam_marks * .8 if rec.total_exam_marks > 0 else 0

    @api.depends('exam_id', 'obtain_marks', 'marks_reeval')
    def _compute_grade(self):
        '''Method to compute grade after re-evaluation'''
        for rec in self:
            grade_lines = rec.exam_id.grade_system.grade_ids
            if (rec.exam_id and rec.exam_id.student_id and grade_lines):
                for grade_id in grade_lines:
                    if rec.obtain_marks and rec.marks_reeval <= 0.0:
                        b_id = rec.obtain_marks <= grade_id.to_mark
                        if (rec.obtain_marks >= grade_id.from_mark and b_id):
                            rec.grade_line_id = grade_id
                    if rec.marks_reeval and rec.obtain_marks >= 0.0:
                        r_id = rec.marks_reeval <= grade_id.to_mark
                        if (rec.marks_reeval >= grade_id.from_mark and r_id):
                            rec.grade_line_id = grade_id

    @api.depends('exam_id', 'subject_id')
    def _compute_highest_marks(self):
        for rec in self:
            marks = []
            exam_id = rec.exam_id.id
            subject_id = rec.subject_id.id
            obj = rec.search([('exam_id', '=', exam_id), ('subject_id', '=', subject_id)])
            for o in obj:
                marks.append(o.obtain_marks)
            rec.highest_marks = max(marks) if len(marks) > 0 else 0


class ParticularReport(models.AbstractModel):
    _name = 'report.report_card.dis_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(docids[0])
        docs = self.env['exam.result'].browse(docids[0])
        # add_result = self.env['exam.subject'].search([('student_id', '=', docs.student_id.id)])
        add_result = self.env['additional.exam.result'].search([('student_id', '=', docs.student_id.id)])
        stu_attendance = self.env['attendance.sheet.line'].search([('roll_no', '=', docs.student_id.id)])

        def _compute_percentage(stu_attendance, att_count=False, percentage=False):
            for attendance_sheet_data in stu_attendance:
                self.att_count = 0
                self.percentage = 0.0
                if attendance_sheet_data.one:
                    att_count = att_count + 1
                if attendance_sheet_data.two:
                    att_count = att_count + 1
                if attendance_sheet_data.three:
                    att_count = att_count + 1
                if attendance_sheet_data.four:
                    att_count = att_count + 1
                if attendance_sheet_data.five:
                    att_count = att_count + 1
                if attendance_sheet_data.six:
                    att_count = att_count + 1
                if attendance_sheet_data.seven:
                    att_count = att_count + 1
                if attendance_sheet_data.eight:
                    att_count = att_count + 1
                if attendance_sheet_data.nine:
                    att_count = att_count + 1
                if attendance_sheet_data.ten:
                    att_count = att_count + 1

                if attendance_sheet_data.one_1:
                    att_count = att_count + 1
                if attendance_sheet_data.one_2:
                    att_count = att_count + 1
                if attendance_sheet_data.one_3:
                    att_count = att_count + 1
                if attendance_sheet_data.one_4:
                    att_count = att_count + 1
                if attendance_sheet_data.one_5:
                    att_count = att_count + 1
                if attendance_sheet_data.one_6:
                    att_count = att_count + 1
                if attendance_sheet_data.one_7:
                    att_count = att_count + 1
                if attendance_sheet_data.one_8:
                    att_count = att_count + 1
                if attendance_sheet_data.one_9:
                    att_count = att_count + 1
                if attendance_sheet_data.one_0:
                    att_count = att_count + 1

                if attendance_sheet_data.two_1:
                    att_count = att_count + 1
                if attendance_sheet_data.two_2:
                    att_count = att_count + 1
                if attendance_sheet_data.two_3:
                    att_count = att_count + 1
                if attendance_sheet_data.two_4:
                    att_count = att_count + 1
                if attendance_sheet_data.two_5:
                    att_count = att_count + 1
                if attendance_sheet_data.two_6:
                    att_count = att_count + 1
                if attendance_sheet_data.two_7:
                    att_count = att_count + 1
                if attendance_sheet_data.two_8:
                    att_count = att_count + 1
                if attendance_sheet_data.two_9:
                    att_count = att_count + 1
                if attendance_sheet_data.two_0:
                    att_count = att_count + 1
                if attendance_sheet_data.three_1:
                    att_count = att_count + 1
                percentage = att_count
                # percentage = round((float(att_count / 31.00) * 100), 2)
            return percentage

        return {
            'doc_model': 'exam.result',
            'data': data,
            'docs': docs,
            'additional_result': add_result,
            'attendance': _compute_percentage(stu_attendance),
            'stu_attendance': stu_attendance
        }
