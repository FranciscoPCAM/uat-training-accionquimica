# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MaintenanceConsumable(models.Model):
    _name = 'maintenance.consumable'
    _description = 'Maintenance Consumable'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', string='Producto', required='1')
    qty = fields.Float(string='Cantidad', required='1')
    product_uom_id = fields.Many2one('uom.uom', string='Unidad de medida del producto', related='product_id.uom_id')
    maintenance_id = fields.Many2one('maintenance.request', string='Maintenance request')
    location_id = fields.Many2one('stock.location', string='Ubicación', domain=[('usage','=','internal')])