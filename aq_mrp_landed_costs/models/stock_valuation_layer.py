# -*- coding: utf-8 -*-

from email.policy import default
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'
    _description = 'Stock Valuation Layer'

    purchase_order_id = fields.Many2one('purchase.order', 
            string="Orden de compra", 
            related="stock_move_id.purchase_line_id.order_id", 
            help="Orden de compra relacionada")
    amount_currency = fields.Monetary('Valor unitario en divisa', readonly=True)
    total_currency = fields.Monetary('Valor total en divisa', readonly=True)
    currency_name = fields.Char(string="Currency name")

    @api.model
    def create(self, vals):
        res = super(StockValuationLayer, self).create(vals)
        for rec in res:
            if rec.purchase_order_id:
                if rec.currency_id.id != rec.stock_move_id.purchase_line_id.currency_id.id:
                    rec.amount_currency = rec.stock_move_id.purchase_line_id.price_unit
                    rec.total_currency = rec.amount_currency * rec.quantity
                    rec.currency_name = rec.purchase_order_id.currency_id.name
        return res