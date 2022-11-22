# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'
    _description = 'Stock Picking Type'

    inter_operation = fields.Boolean(string="Internacional", help="Marcar como verdadero si la operación es de recepción internacional")