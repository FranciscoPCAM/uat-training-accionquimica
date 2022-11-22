# -*- coding: utf-8 -*-

from email.policy import default
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

# class StockPickingFleet(models.Model):
#     _inherit = 'stock.picking'
#     _description = 'Stock Picking Fleet'

#     fleet_vehicle_id = fields.Many2one('fleet.vehicle', string="Unidad de flota")
#     license_plate = fields.Char(string="Matrícula", related="fleet_vehicle_id.license_plate")
#     driver_id = fields.Many2one('res.partner', string="Chofer", related="fleet_vehicle_id.driver_id")
#     date_filter = fields.Date(string="Date filter", default=fields.date.today())

#     @api.onchange('fleet_vehicle_id')
#     def onchange_fleet_vehicle_id(self):
#         if self.fleet_vehicle_id:
#             self.l10n_mx_edi_vehicle_id = self.fleet_vehicle_id.l10n_mx_edi_vehicle_id.id

#     def button_validate(self):
#         # res = super(AccountMove, self).write(vals)
#         if not self.fleet_vehicle_id:
#             raise ValidationError(_("Es necesario definir un vehículo para esta transferencia."))
#         return super(StockPickingFleet, self).button_validate()
