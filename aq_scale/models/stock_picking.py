# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPickingScale(models.Model):
    _inherit = 'stock.picking'
    _description = 'Stock Picking'

    scale_id = fields.Many2one('scale.data', string="Datos del pesaje")
    tare_weight = fields.Char(string="Peso tara", related="scale_id.tare_weight")
    gross_weight = fields.Char(string="Peso bruto", related="scale_id.gross_weight")
    net_weight = fields.Char(string="Peso Neto", related="scale_id.net_weight")
    create_date = fields.Datetime(string="Fecha", related="scale_id.create_date")
    departure_date = fields.Datetime(string="Hora de salida", related="scale_id.departure_date")