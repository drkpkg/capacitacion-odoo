# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    can_be_rented = fields.Boolean(string="Se puede reservar", default=False)
