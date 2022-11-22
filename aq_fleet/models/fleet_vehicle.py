# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'Fleet Vehicle'

    l10n_mx_edi_vehicle_id = fields.Many2one('l10n_mx_edi.vehicle', 
    string="Configuración del vehículo")
    picking_count = fields.Integer(compute="_compute_picking_count", string="Picking History Count")
    picking_cancel_count = fields.Integer(compute="_compute_picking_count", string="Picking Cancel History Count")
    fuel_count = fields.Integer(compute="_compute_fuel_count", string="Fuel History Count")

    def _compute_picking_count(self):
        picking_obj = self.env['stock.picking']
        for record in self:
            record.picking_count = picking_obj.search_count([('fleet_vehicle_id', '=', record.id)])
            record.picking_cancel_count = picking_obj.search_count([('fleet_vehicle_id', '=', record.id),'|',('state', '=', 'cancel'),('picking_type_id.name','in',('Devoluciones','Returns'))])

    def _compute_fuel_count(self):
        picking_obj = self.env['fleet.vehicle.log.services']
        for record in self:
            record.fuel_count = picking_obj.search_count([('vehicle_id', '=', record.id),('service_type_id', '=', self.env.ref('aq_fleet.fuel_service_data').id)])

    def open_picking_recs(self):
        # action = self.env.ref('stock.action_picking_tree_all')
        action = self.env.ref('aq_fleet.action_picking_smart_button')
        result = action.read()[0]
        picking_ids = self.env['stock.picking'].search([('fleet_vehicle_id','=',self.id)])
        #choose the view_mode accordingly
        # if len(picking_ids) != 1:
        #     result['domain'] = "[('id', 'in', " + str(picking_ids.ids) + ")]"
        # elif len(picking_ids) == 1:
        #     res = self.env.ref('stock.view_picking_form', False)
        #     result['views'] = [(res and res.id or False, 'form')]
        #     result['res_id'] = picking_ids.id
        # result['domain'] = "[('id', 'in', " + str(picking_ids.ids) + ")]"
        return result

    def cancel_picking_recs(self):
        action = self.env.ref('aq_fleet.action_cancel_picking_smart_button')
        result = action.read()[0]
        picking_ids = self.env['stock.picking'].search([('fleet_vehicle_id','=',self.id),'|',('state','=','cancel'),('picking_type_id.name','in',('Devoluciones','Returns'))])
        result['domain'] = "[('id', 'in', " + str(picking_ids.ids) + ")]"
        return result

    def fuel_service_action(self):
        action = self.env.ref('aq_fleet.action_fuel_smart_button')
        result = action.read()[0]
        vehicle_services_ids = self.env['fleet.vehicle.log.services']\
            .search([('vehicle_id','=',self.id),\
            ('service_type_id', '=', self.env.ref('aq_fleet.fuel_service_data').id)])
        result['domain'] = "[('id', 'in', " + str(vehicle_services_ids.ids) + ")]"
        ctx = result['context']
        result['context'] = ctx[:25] + ", 'default_service_type_id': " +\
            str(self.env.ref('aq_fleet.fuel_service_data').id) +\
            ", 'default_vehicle_id': " + str(self.id) +\
            ", 'default_purchaser_id': " + str(self.driver_id.id) + '}'
        return result