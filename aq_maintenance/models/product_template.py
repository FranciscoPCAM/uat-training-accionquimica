# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    # is_consumable = fields.Boolean(string='Es consumible')
    equipment_ids = fields.Many2many('maintenance.equipment', string='Equipos')
    criticality_id = fields.Many2one('maintenance.criticality', string='Criticidad')