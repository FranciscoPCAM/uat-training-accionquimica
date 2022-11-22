# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        res = super(PurchaseOrderLine, self).onchange_product_id()
        for line in self:
            if line.product_id:
                line.order_id._currency_validation(line)
                #PCI: Validation commented, the requirements need to be validated.
                # line.order_id._pricelist_validation(line)
        return res

    @api.onchange('product_qty')
    def onchange_product_qty(self):
        for line in self:
            if line.product_id:
                packaging =  line.product_id.packaging_ids
                items = filter(lambda x: (x.qty == line.product_qty), packaging)
                items = list(items)
                if not items or line.product_qty == 0 or not line.product_qty:
                    return {
                        'warning': {
                            'title': _("Advertencia"),
                            'message': _("Ojo: Revisa las cantidades, parece que no hay una presentación de venta compatible."),
                        }
                    }