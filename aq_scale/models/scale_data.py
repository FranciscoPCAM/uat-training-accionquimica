# -*- coding: utf-8 -*-

from email.policy import default
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ScaleData(models.Model):
    _name = 'scale.data'
    _description = 'Scale General Data'
    _rec_name = 'create_date'

    def _default_today_datetime(self):
        return fields.Datetime.now(self)

    name = fields.Char(string="name", default="Bascula")
    tare_weight = fields.Char(string="Peso tara")
    gross_weight = fields.Char(string="Peso bruto")
    net_weight = fields.Char(string="Peso neto")
    create_date = fields.Datetime(string="Fecha", default=_default_today_datetime)
    departure_date = fields.Datetime(string="Hora de salida")
    picking_ids = fields.One2many('stock.picking','scale_id',string="Pickings")