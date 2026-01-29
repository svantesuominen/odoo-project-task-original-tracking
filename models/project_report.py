# -*- coding: utf-8 -*-
from odoo import fields, models

class ReportProjectTaskUser(models.Model):
    _inherit = "report.project.task.user"

    deadline_diff = fields.Integer("Deadline Difference (Days)", readonly=True)
    allocated_hours_diff = fields.Float("Planned Hours Difference", readonly=True)
    remaining_original_hours = fields.Float("Remaining Original Hours", readonly=True)

    def _select(self):
        return super()._select() + """,
            t.deadline_diff,
            t.allocated_hours_diff,
            t.remaining_original_hours
        """

    def _group_by(self):
        return super()._group_by() + """,
            t.deadline_diff,
            t.allocated_hours_diff,
            t.remaining_original_hours
        """
