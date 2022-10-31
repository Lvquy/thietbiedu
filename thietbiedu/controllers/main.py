# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Thietbiedu(http.Controller):

    @http.route(['/google51aebbe99d6bf534.html'], auth='public', website=True)
    def google_search(self, **kw):
        return request.render('thietbiedu.google51aebbe99d6bf534')