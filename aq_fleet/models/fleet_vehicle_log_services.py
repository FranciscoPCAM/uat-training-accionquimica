# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FleetVehicleLogServices(models.Model):
    _inherit = 'fleet.vehicle.log.services'
    _description = 'Fleet Vehicle Log Services'

    is_planned = fields.Boolean(string="Servicio planeado")
    purchase_order_id = fields.Many2one('purchase.order',string="Orden de compra")
    expense_id = fields.Many2one('hr.expense',string="Gasto")