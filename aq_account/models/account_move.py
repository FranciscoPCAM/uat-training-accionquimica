# -*- coding: utf-8 -*-

from email.policy import default
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = 'Account move inherit'

    def _default_rate(self):
        banamex_obj = self.env['banamex.currency'].search([], limit=1)
        return banamex_obj.id

    @api.depends('banamex_currency_id')
    def _banamex_amount(self):
        for rec in self:
            rec.amount_total_banamex = rec.amount_total * rec.banamex_currency_id.inverse_company_rate

    @api.depends('invoice_origin')
    def _is_sale_order(self):
        for rec in self:
            if rec.invoice_origin:
                if 'S0' in (rec.invoice_origin):
                    rec.is_sale_order = True
                else:
                    rec.is_sale_order = False
            else:
                rec.is_sale_order = False

    banamex_currency_id = fields.Many2one('banamex.currency', string="Tipo de cambio citibanamex", default=_default_rate)
    banamex_historic_currency_id = fields.Many2one('banamex.currency', string="Tipo de cambio citibanamex")
    related_currency_id = fields.Integer(string="Campo auxiliar", related="currency_id.id")
    amount_total_banamex = fields.Monetary(string="Total cobro USD", compute="_banamex_amount")
    is_scale = fields.Boolean(string="Existe pesaje?")
    is_sale_order = fields.Boolean(string="Existe orden de venta?", compute="_is_sale_order")

    def write(self, vals):
        payment_state = vals.get('payment_state', False)
        res = super(AccountMove, self).write(vals)
        if payment_state:
            self.banamex_historic_currency_id = self.banamex_currency_id.id
        return res