# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class BanamexCurrency(models.Model):
    _name = 'banamex.currency'
    _inherit = 'res.currency.rate'
    _description = 'Banamex currency rate'

    def name_get(self):
        result = []

        for rec in self:
            result.append((rec.id, '%s - %s %s' % (rec.name,rec.inverse_company_rate,rec.currency_id.name)))
        return result

    @api.model
    def create(self, vals):
        res = super(BanamexCurrency, self).create(vals)
        rate_obj = res.env['banamex.currency'].search([], limit=1)
        if rate_obj:
            invoice_obj = res.env['account.move'].search([('state','in',['draft','posted'])])
            if invoice_obj:
                for invoices in invoice_obj:
                    invoices.banamex_currency_id = rate_obj.id
        return res

    def write(self, vals):
        res = super(BanamexCurrency, self).write(vals)
        rate_obj = self.env['banamex.currency'].search([], limit=1)
        if rate_obj:
            invoice_obj = self.env['account.move'].search([('state','in',['draft','posted'])])
            if invoice_obj:
                for invoices in invoice_obj:
                    invoices.banamex_currency_id = rate_obj.id
        return res