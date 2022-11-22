# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Order'

    #PCI: utils functions

    def _pricelist_validation(self, rec):
        product_pricelist =  rec.order_id.partner_id.property_product_pricelist.item_ids
        items = filter(lambda x: (x.product_tmpl_id.id == rec.product_id.product_tmpl_id.id), product_pricelist)
        items = list(items)
        if not items:
            raise ValidationError(_("El producto seleccionado no está disponible en la lista de precio. Favor de definir primero su precio correspondiente."))
        return True

    def _currency_validation(self, rec):
            if rec.product_id.main_currency_id.id != rec.order_id.currency_id.id:
                raise ValidationError(_("El producto no puede ser procesado con esta moneda, es exclusivo para '%s'.") % (rec.product_id.currency_id.name,))
            return True

    def _currency_multiple_validation(self, rec):
        if rec.product_id.main_currency_id.id != rec.currency_id.id:
            product_name = rec.product_id.name
            if rec.product_id.default_code:
                product_name = '['+rec.product_id.default_code+']' + ' ' + rec.product_id.name
            raise ValidationError(_("El producto '%s' no puede ser procesado con esta moneda, es exclusivo para '%s'.") % (product_name, rec.product_id.currency_id.name,))
        return True


    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        for line in res.order_line:
            if line.product_id:
                line.order_id._currency_multiple_validation(line)
                #PCI: Validation commented, the requirements need to be validated.
                # line.order_id._pricelist_validation(line)
        return res

    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)
        for line in self.order_line:
            if line.product_id:
                line.order_id._currency_multiple_validation(line)
                #PCI: Validation commented, the requirements need to be validated.
                # line.order_id._pricelist_validation(line)
        return res