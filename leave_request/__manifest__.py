{
    'name': "HR Leave Request",
    'summary': """Create Leave Requests for Employees""",
    'description': """HR Leave Request
    ================================
    
    
    Dev Log:
    * Create model leave.request for requesting leaves
    * Create model leave.request.type for selection of leaves type
    
    """,
    'license': 'OPL-1',
    'author': 'Calvin-C-M',
    'version': '0.0.1',
    'website': 'www.example.com',
    'category': 'Human Resources/Time Off',
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/leave_type_views.xml',
        'views/leave_request_views.xml',
        'views/leave_request_menuitems.xml',
    ],
    'application': True
}