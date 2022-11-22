# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sales Order'

    client_oc = fields.Char(string="OC del cliente")

    #PCI: utils functions

    def _pricelist_validation(self, rec):
        product_pricelist =  rec.order_id.pricelist_id.item_ids
        items = filter(lambda x: (x.product_id.id == rec.product_id.id), product_pricelist)
        items = list(items)
        if not items:
            raise ValidationError(_("El producto seleccionado no está disponible en la lista de precio. Favor de definir primero su precio correspondiente."))
        return True

    def _currency_validation(self, rec):
            if rec.product_id.main_currency_id.id != rec.order_id.pricelist_id.currency_id.id:
                raise ValidationError(_("El producto no puede ser procesado con esta moneda, es exclusivo para '%s'.") % (rec.product_id.currency_id.name,))
            return True

    def _currency_multiple_validation(self, rec):
        if rec.product_id.main_currency_id.id != rec.order_id.pricelist_id.currency_id.id:
            product_name = rec.product_id.name
            if rec.product_id.default_code:
                product_name = '['+rec.product_id.default_code+']' + ' ' + rec.product_id.name
            raise ValidationError(_("El producto '%s' no puede ser procesado con esta moneda, es exclusivo para '%s'.") % (product_name, rec.product_id.currency_id.name,))
        return True


    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        for line in res.order_line:
            if line.product_id:
                line.order_id._currency_multiple_validation(line)
                line.order_id._pricelist_validation(line)
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        for line in self.order_line:
            if line.product_id:
                line.order_id._currency_multiple_validation(line)
                line.order_id._pricelist_validation(line)
        return res

    def _action_confirm(self):
        """ Extends method for partener data validation.
        """
        res = super(SaleOrder, self)._action_confirm()
        for order in self:
            switch, data = order.check_partner_data(order.partner_id)
            if not switch:
                msg = ''
                for item in data:
                    if msg == '':
                        msg = '\n'
                    msg = msg + '- ' + item + '\n'
                raise ValidationError(_("Favor de completar la siguiente información del cliente para poder validar el pedido de venta '%s'.") % (msg,))
            if not order.client_oc:
                raise ValidationError(_("Añadir referencia de OC de cliente."))

        return res

    def check_partner_data(self, partner):
        """ This method make a data validation for res.partner.
            Return True on success case.
            Return False and unfilled fields on fail case.
        """
        data_checked = []
        if partner.company_type == 'company':
            if not partner.parent_id:
                data_checked = self.parent_data(partner, data_checked)
            else:
                data_checked = self.child_data(partner, data_checked)
        else:
            if not partner.parent_id:
                data_checked = self.parent_data(partner, data_checked)
            else:
                data_checked = self.child_data(partner, data_checked)

        if data_checked:
            return False, data_checked
        else:
            return True, ''

    def parent_data(self, parent, data):
        if not parent.name:
            data.append('Razón social')
        if not parent.vat:
            data.append('Razón social')
        if not parent.street:
            data.append('Domicilio')
        if not parent.phone:
            data.append('Teléfono')
        if not parent.industry_id:
            data.append('Industria')
        if not parent.customer_class:
            data.append('Clasificación')
        if not parent.bank_ids:
            data.append('Banco')
            data.append('Número de cuenta')
        else:
            if not parent.bank_ids[0].bank_id:
                data.append('Banco')
            if not parent.bank_ids[0].acc_number:
                data.append('Número de cuenta')
        return data

    def child_data(self, child, data):
        if not child.name or not child.parent_id.name:
            data.append('Razón social')
        if not child.parent_id.vat:
            data.append('Razón social')
        if not child.street_name:
            data.append('Domicilio')
        if not child.phone:
            data.append('Teléfono')
        if not child.parent_id.industry_id:
            data.append('Industria')
        if not child.customer_class:
            data.append('Clasificación')
        if not child.parent_id.bank_ids:
            data.append('Banco')
            data.append('Número de cuenta')
        else:
            if not child.parent_id.bank_ids[0].bank_id:
                data.append('Banco')
            if not child.parent_id.bank_ids[0].acc_number:
                data.append('Número de cuenta')
        return data