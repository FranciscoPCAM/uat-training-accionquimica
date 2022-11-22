# -*- coding: utf-8 -*-

from email.policy import default
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = 'Account move line inherit'

    is_scale = fields.Boolean(string="Existe pesaje?", related="move_id.is_scale")
    is_sale_order = fields.Boolean(string="Existe order de venta?", related="move_id.is_sale_order")