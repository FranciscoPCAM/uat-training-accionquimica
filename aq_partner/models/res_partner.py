# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Main contacts module'

    custom_product_pricelist = fields.Many2many(
        'product.pricelist', string="Lista de precios",
        domain=lambda self: [('is_allowed','=',True)])
        # domain=lambda self: [('company_id', 'in', (self.env.company.id, False)),('is_allowed','=',True)])

    def _default_payment_term(self):
        default_value = self.env['account.payment.term'].search([('is_default', '=', True)], limit=1)
        return default_value.id

    customer_class = fields.Selection([
        ('consu', 'Consumidor'),
        ('comer', 'Comercializador')],string="Clasificación de cliente")
    property_supplier_payment_term_id = fields.Many2one('account.payment.term', default=_default_payment_term, required=True)
    property_payment_term_id = fields.Many2one('account.payment.term', default=_default_payment_term, required=True)
    product_ids = fields.Many2many('product.product',
        string="Productos mas vendidos", 
        domain=[('sale_ok', '=', 1)])
    max_debt = fields.Monetary(string="Deuda Máxima")
    days_limit_debt = fields.Integer(string="Saldo vencido", default=0)
    max_balance = fields.Many2one('account.payment.term',string="Saldo vencido")