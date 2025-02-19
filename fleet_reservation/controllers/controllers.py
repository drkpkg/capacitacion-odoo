# -*- coding: utf-8 -*-
from odoo import http
import json


class FleetReservation(http.Controller):
    def _build_reservation(self, reservation):
        return {
            "id": reservation.id,
            "name": reservation.name,
            "vehicle_id": reservation.vehicle_id.name,
            "customer_id": reservation.customer_id.name,
            "start_date": reservation.start_date.strftime("%d/%m/%Y"),
            "end_date": reservation.end_date.strftime("%d/%m/%Y"),
            "state": reservation.state,
        }

    def _to_json(self, arr_list):
        return json.dumps(arr_list)

    @http.route("/fleet_reservation/while_loop", auth="public")
    def fleet_reservation_while_loop(self, **kw):
        reservation_ids = http.request.env["fleet.reservation"].search([])
        result = []
        current_position = 0
        while current_position < len(reservation_ids):
            reservation = reservation_ids[current_position]
            result.append(self._build_reservation(reservation))
            current_position += 1
        return self._to_json(result)

    @http.route("/fleet_reservation/for_loop", auth="public")
    def fleet_reservation_for_loop(self, **kw):
        reservation_ids = http.request.env["fleet.reservation"].search([])
        result = []
        for reservation in reservation_ids:
            result.append(self._build_reservation(reservation))
        return self._to_json(result)

    @http.route("/fleet_reservation/optimized", auth="public")
    def fleet_reservation_optimized(self, **kw):
        reservation_ids = http.request.env["fleet.reservation"].search([])
        return json.dumps(
            [
                {
                    "id": reservation.id,
                    "name": reservation.name,
                    "vehicle_id": reservation.vehicle_id.name,
                    "customer_id": reservation.customer_id.name,
                    "start_date": reservation.start_date.strftime("%d/%m/%Y"),
                    "end_date": reservation.end_date.strftime("%d/%m/%Y"),
                    "state": reservation.state,
                }
                for reservation in reservation_ids
            ]
        )
