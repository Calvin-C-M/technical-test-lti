from odoo import api, fields, models


class LeaveType(models.Model):
    _name = 'leave.type'
    _description = 'Types of leave available'

    name = fields.Char(string='Leave Name')
    description = fields.Text(string='Description')
