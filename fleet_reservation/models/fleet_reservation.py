from odoo import models, fields, api


class FleetReservation(models.Model):
    _name = "fleet.reservation"
    _description = "Reserva de Vehículo"

    name = fields.Char(
        string="Nombre de la Reserva",
        required=True,
        compute="_compute_name",
        store=True,
    )
    vehicle_id = fields.Many2one(
        "fleet.vehicle",
        string="Vehículo",
        required=True,
    )
    customer_id = fields.Many2one("res.partner", string="Cliente", required=True)
    start_date = fields.Date(string="Fecha de Inicio", required=True)
    end_date = fields.Date(string="Fecha de Finalización", required=True)
    state = fields.Selection(
        [
            ("draft", "Borrador"),
            ("confirmed", "Confirmado"),
            ("cancelled", "Cancelado"),
        ],
        string="Estado",
        default="draft",
        required=True,
    )

    @api.depends("vehicle_id", "customer_id")
    def _compute_name(self):
        for reservation in self:
            if reservation.vehicle_id and reservation.customer_id:
                name = f"{reservation.vehicle_id.name} - {reservation.customer_id.name}"
                reservation.name = name    
            else:
                reservation.name = "Nueva Solicitud"