# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    _description = 'Stock Picking'

    inter_operation = fields.Boolean(string="Internacional", related='picking_type_id.inter_operation')