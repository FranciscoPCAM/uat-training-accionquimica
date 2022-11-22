# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    def _default_user(self):
        ctx = self.env.context.copy()
        uid = ctx.get('uid', False)
        if uid:
            return uid

    main_currency_id = fields.Many2one('res.currency', string="Moneda principal", required=1)
    data_sheet = fields.Char(string="Ficha Técnica")
    safe_sheet = fields.Char(string="Hoja de datos de seguridad")
    transport_sheet = fields.Char(string="Emergencia de transportación")
    create_date = fields.Datetime(default=fields.Date.today())
    create_uid = fields.Many2one('res.users',default=_default_user)
    formula = fields.Char(string="Fórmula")
    physical_state = fields.Char(string="Estado físico")
    appearance = fields.Char(string="Apariencia")
    other_name = fields.Char(string="Otros nombres")
    use = fields.Char(string="Usos")
    web_description = fields.Text(string="Descripción del producto")