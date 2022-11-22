# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Sales Order Line'

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        for line in self:
            if line.product_id:
                line.order_id._currency_validation(line)
                line.order_id._pricelist_validation(line)
        return res

    @api.onchange('product_uom_qty')
    def onchange_product_uom_qty(self):
        for line in self:
            if line.product_id:
                packaging =  line.product_id.packaging_ids
                items = filter(lambda x: (x.qty == line.product_uom_qty), packaging)
                items = list(items)
                if not items or line.product_uom_qty == 0 or not line.product_uom_qty:
                    return {
                        'warning': {
                            'title': _("Advertencia"),
                            'message': _("Ojo: Revisa las cantidades, parece que no hay una presentación de venta compatible."),
                        }
                    }