from odoo import api, fields, models


class LeaveRequest(models.Model):
    _name = 'leave.request'
    _description = 'Request a time off for an employee'

    # def _default_employee_id(self):
    #     return

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    employee_id = fields.Many2one(comodel_name='hr.employee',
                                  string='Employee',
                                  required=True
                                  # default=_default_employee_id
                                  )
    leave_type_id = fields.Many2one(comodel_name='leave.type', required=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
    ], string='Status', default='draft', required=True)
    days_count = fields.Integer(string='How Long?')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(required=True)

    def action_request(self):
        for rec in self:
            rec.state = 'pending'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_reject(self):
        for rec in self:
            rec.state = 'reject'
