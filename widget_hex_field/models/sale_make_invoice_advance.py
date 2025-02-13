from odoo import models, fields, api, _


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoices(self, sale_orders):
        invoice_id = super()._create_invoices(sale_orders)
        invoice_id.update({"hex_field": sale_orders.hex_field})
        return invoice_id
