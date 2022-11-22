# -*- coding: utf-8 -*-

import logging
import json

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'
    _description = 'Sales Order'

    partner_button = fields.Char(string="Cliente", related='partner_id.name')
    partner_inv_button = fields.Char(string="Dirección de factura", related='partner_invoice_id.name')
    partner_ship_button = fields.Char(string="Dirección de entrega", related='partner_shipping_id.name')

    def partner_button_action(self):
        """ 
        Opens a new partner view in readonly mode

        """
        action = self.env.ref('aq_sale.action_partner_customer')
        result = action.read()[0]
        res = self.env.ref('base.view_partner_form', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['res_id'] = self.partner_id.id
        return result

    def partner_inv_button_action(self):
        """ 
        Opens a new partner view in readonly mode

        """
        action = self.env.ref('aq_sale.action_partner_customer')
        result = action.read()[0]
        res = self.env.ref('base.view_partner_form', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['res_id'] = self.partner_invoice_id.id
        return result

    def partner_ship_button_action(self):
        """ 
        Opens a new partner view in readonly mode

        """
        action = self.env.ref('aq_sale.action_partner_customer')
        result = action.read()[0]
        res = self.env.ref('base.view_partner_form', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['res_id'] = self.partner_shipping_id.id
        return result

    @api.onchange('pricelist_id','partner_id')
    def _onchange_pricelist_id_domain(self):
        for rec in self:
            if self.partner_id.custom_product_pricelist.ids:
                partner_pricelist = self.partner_id.custom_product_pricelist.ids
            elif self.company_id.custom_product_pricelist.ids:
                partner_pricelist = self.company_id.custom_product_pricelist.ids
            else:
                raise ValidationError(_("Es necesario definir listas de precios por defecto en la ficha de la empresa."))
            domain = [('id', 'in', partner_pricelist)]
            return {'domain': {'pricelist_id': domain}}

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrderCustom, self).onchange_partner_id()
        for rec in self:
            rec.update({'pricelist_id': False})
            if rec.partner_id:
                if rec.partner_id.max_debt != 0.00:
                    switch, msg = self._max_debt_validation(rec.partner_id, 0.00)
                    if switch:
                        return {
                            'warning': {
                                'title': _("Advertencia"),
                                'message': _(msg),
                            }
                        }
                # ctx = self._context
                # user_id = ctx.get('uid')
                if not rec.partner_id.user_id.id == self.user_id.id:
                    raise ValidationError(_("Este cliente tiene un vendedor diferente asignado, favor de seleccionarlo."))

    def _create_invoices(self, grouped=False, final=False, date=None):
        """
            Handles forcasted quantities before create a new invoice.
        """
        for lines in self.order_line:
            if lines.product_id.detailed_type == 'product':
                forcasted_qty = lines.product_id.virtual_available
                if forcasted_qty < lines.product_uom_qty:
                    raise ValidationError(_("Las cantidades pronosticadas para el producto %s no son suficientes para crear la factura.") % (lines.product_id.name,))

        return super(SaleOrderCustom, self)._create_invoices(grouped,final,date)

    @api.onchange('amount_total')
    def _onchange_amount_total_debt(self):
        for rec in self:
            if rec.amount_total:
                switch, msg = self._max_debt_validation(rec.partner_id, rec.amount_total)
                if switch:
                    return {
                        'warning': {
                            'title': _("Advertencia"),
                            'message': _(msg),
                        }
                    }

    def _action_confirm(self):
        """ 
            Extends method for partner max debt validation.
        """
        switch, msg = self._max_debt_validation(self.partner_id, self.amount_total)
        if switch:
            raise ValidationError(_(msg))

        return super(SaleOrderCustom, self)._action_confirm()

    def _max_debt_validation(self, partner, amount_total):
        cont = 0.00
        is_amount_total_debt = False
        is_days_max_debt = False
        order_warning = 'El monto total de la cotización excede el límite de Deuda Máxima definido para el cliente.'
        partner_warning = 'El cliente ha excedido los límites de Deuda ó Saldo Vencido.'
        partner_date_warning = 'La antigüedad de la deuda excedió el límite para el Saldo Vencido.'
        unpaid_invoices = self.env['account.move'].search([('partner_id','=',partner.id),('state','=','posted'),('payment_state','not in',('paid','reversed','invoicing_legacy')),('move_type','=','out_invoice')])
        for inv_item in unpaid_invoices:
            cont += inv_item.amount_residual
            if inv_item.invoice_date_due < fields.date.today():
                debt_days = fields.date.today() - inv_item.invoice_date_due
                if debt_days.days >= partner.days_limit_debt:
                    is_days_max_debt = True
        is_partner_max_debt = True if cont > partner.max_debt else False
        if amount_total != 0.00:
            is_amount_total_debt = True if cont + amount_total >= partner.max_debt else False
        if is_partner_max_debt and not is_days_max_debt:
            return True, partner_warning
        elif is_partner_max_debt and is_days_max_debt:
            return True, partner_warning
        elif not is_partner_max_debt and is_days_max_debt:
            return True, partner_date_warning
        elif is_amount_total_debt:
            return True, order_warning
        else:
            return False, ''