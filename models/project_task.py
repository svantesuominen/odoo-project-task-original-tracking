# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import timedelta

class Task(models.Model):
    _inherit = 'project.task'

    original_date_deadline = fields.Datetime("Original Deadline", copy=False, groups="project.group_project_manager")
    original_allocated_hours = fields.Float("Originally Planned Hours", copy=False, groups="project.group_project_manager")

    deadline_diff = fields.Integer("Deadline Difference (Days)", compute='_compute_deadline_diff', store=True, help="Difference between current deadline and original deadline in days.")
    allocated_hours_diff = fields.Float("Planned Hours Difference", compute='_compute_allocated_hours_diff', store=True, help="Difference between current allocated hours and original allocated hours.")
    remaining_original_hours = fields.Float("Remaining Original Hours", compute='_compute_remaining_original_hours', store=True, help="Hours remaining from the original plan. (Original Plan - Spent Hours)")

    @api.depends('date_deadline', 'original_date_deadline')
    def _compute_deadline_diff(self):
        for task in self:
            if task.date_deadline and task.original_date_deadline:
                # Calculate difference in days
                diff = task.date_deadline - task.original_date_deadline
                task.deadline_diff = diff.days
            else:
                task.deadline_diff = 0

    @api.depends('allocated_hours', 'original_allocated_hours')
    def _compute_allocated_hours_diff(self):
        for task in self:
            task.allocated_hours_diff = task.allocated_hours - task.original_allocated_hours

    @api.depends('effective_hours', 'original_allocated_hours')
    def _compute_remaining_original_hours(self):
        for task in self:
            # Remaining from original budget = Original Plan - Hours Spent
            task.remaining_original_hours = task.original_allocated_hours - task.effective_hours

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('date_deadline') and not vals.get('original_date_deadline'):
                vals['original_date_deadline'] = vals['date_deadline']
            if vals.get('allocated_hours') and not vals.get('original_allocated_hours'):
                vals['original_allocated_hours'] = vals['allocated_hours']
        return super(Task, self).create(vals_list)

    def write(self, vals):
        for task in self:
            # If original_date_deadline is not set and we are setting a deadline now
            if 'date_deadline' in vals and not task.original_date_deadline and vals.get('date_deadline'):
                # Only set it if it's not explicitly being set in this write call by an admin
                if 'original_date_deadline' not in vals:
                    vals['original_date_deadline'] = vals['date_deadline']
            
            # If original_allocated_hours is not set and we are setting allocated hours now
            if 'allocated_hours' in vals and not task.original_allocated_hours and vals.get('allocated_hours'):
                if 'original_allocated_hours' not in vals:
                    vals['original_allocated_hours'] = vals['allocated_hours']
                
        return super(Task, self).write(vals)
