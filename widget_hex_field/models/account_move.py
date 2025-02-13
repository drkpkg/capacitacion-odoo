from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    hex_field = fields.Char(string="Hex Field", copy=False)
