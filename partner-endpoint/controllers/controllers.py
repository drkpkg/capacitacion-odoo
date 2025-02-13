# -*- coding: utf-8 -*-
from odoo import http

class ResPartner(http.Controller):
    @http.route('/partners', auth='public', methods=['GET'], csrf=False)
    def index(self, **kw):
        partners = http.request.env['res.partner'].sudo().search([])
        return str({'partners': [(partner.id, partner.name) for partner in partners] })
