import json
import logging
import werkzeug

from odoo import http
from odoo.http import request
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class LeaveRequestControllers(http.Controller):

    def _prepare_response(self, status="", message="", data=None):
        return {
            'status': status,
            'message': message,
            'data': data
        }

    def _prepare_leave_request_data(self, id):
        LeaveRequest = request.env['leave.request']
        data = LeaveRequest.sudo().search([('id', '=', id)], limit=1)
        return {
            'id': data.id,
            'name': data.name,
            'description': data.description,
            'employee': data.employee_id.name,
            'start_date': data.start_date.strftime('%Y-%m-%d'),
            'end_date': data.end_date.strftime('%Y-%m-%d'),
            'state': data.state,
        }

    @http.route('/leave-request', methods=['POST', 'PUT'], auth='public', type='json')
    def update_leave_request(self, **kwargs):
        response = self._prepare_response()
        data = request.jsonrequest

        try:
            id = data.get('id')
            state = data.get('state')

            data = request.env['leave.request'].search([('id', '=', id)])
            if not data:
                raise UserError("The requested ID not found")

            data.write({
                'id': id,
                'state': state,
            })
        except:
            response['status'] = 'ERROR'

        return request.make_response(
            headers={'Content-Type': 'application/json'},
            data=http.Response(json.dumps(response)).data
        )

    @http.route('/leave-request/<int:leave_id>', methods=['GET'], auth='public')
    def get_leave_request(self, leave_id, **kwargs):
        response = self._prepare_response('SUCCESS', '')

        try:
            leave_rec = self._prepare_leave_request_data(leave_id)
            response['data'] = leave_rec
        except:
            response['status'] = 'ERROR'
            response['message'] = 'There is an error from the server'

        return request.make_response(
            headers={'Content-Type': 'application/json'},
            data=http.Response(json.dumps(response)).data
        )
