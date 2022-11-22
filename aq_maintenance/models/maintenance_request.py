# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'
    _description = 'Maintenance Request'

    consumable_ids = fields.One2many('maintenance.consumable','maintenance_id', string='Consumibles')
    consumable_visibility = fields.Boolean(string="Hide button?",related='stage_id.done')
    consumable_used = fields.Boolean(string="Button used?")

    def run_stock_quant(self):
        if not self.consumable_ids:
            raise ValidationError(_("Debe seleccionar al menos un consumible."))
        self.write({'consumable_used': True})
        item_vals = []
        quant_vals = {}
        aux = 0
        ctx = self.env.context.copy()
        uid = ctx.get('uid', False)
        in_date = fields.date.today()
        for consumable in self.consumable_ids:
            # quant_ids = filter(lambda x: (x.available_quantity >= consumable.qty and x.usage == 'internal'), consumable.product_id.stock_quant_ids)
            quant_ids = filter(lambda x: (x.location_id.id == consumable.location_id.id), consumable.product_id.stock_quant_ids)
            quant_ids = list(quant_ids)
            if len(quant_ids) > 0 and quant_ids[0].available_quantity >= consumable.qty:
                quant_vals['product_id'] = consumable.product_id.id
                quant_vals['reserved_quantity'] = consumable.qty
                quant_vals['quantity'] = consumable.qty * -1
                quant_vals['product_uom_id'] = consumable.product_uom_id.id
                quant_vals['location_id'] = consumable.location_id.id
                quant_vals['in_date'] = in_date
                quant_vals['user_id'] = uid
                item_vals.append(quant_vals)
                quant_vals = {}
            else:
                aux += 1
        if aux > 0:
            raise ValidationError(_("No hay productos suficientes para el mantenimiento."))
        else:
            for vals in item_vals:
                self.env['stock.quant'].create(vals)
        return True