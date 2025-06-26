from odoo import http
from odoo.http import request , route

class AwesomeOwl(http.Controller):

    @http.route(['/awesome_owl'], type='http', auth='public')
    def show_my_asset(self):
        return request.render('awesome_owl.awesome')