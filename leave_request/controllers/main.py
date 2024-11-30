import json
import logging
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class LeaveRequestControllers(http.Controller):

    def _prepare_response(self, status="", message="", data=None):
        return {
            'status': status,
            'message': message,
            'response': data
        }

    # def _prepare_leave_request_data(self):


    @http.route('/leave-request', methods=['POST', 'PUT'], auth='public')
    def update_leave_request(self, leave_id, **kwargs):
        pass

    @http.route('/leave-request/<int:leave_id>', methods=['GET'], auth='public')
    def get_leave_request(self, leave_id, **kwargs):
        LeaveRequest = request.env['leave.request']
        response = self._prepare_response('SUCCESS', '')

        try:
            leave_rec = LeaveRequest.sudo().browse(leave_id)
            response['data'] = leave_rec
        except:
            response['status'] = 'ERROR'
            response['message'] = 'There is an error from the server'

        return request.make_response(
            headers={'Content-Type': 'application/json'},
            data=http.Response(json.dumps(response)).data
        )
