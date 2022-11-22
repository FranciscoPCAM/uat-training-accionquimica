# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ResCompanyCustom(models.Model):
    _inherit = 'res.company'
    _description = 'Res Company'

    custom_product_pricelist = fields.Many2many(
        'product.pricelist', string="Lista de precios", required=1)