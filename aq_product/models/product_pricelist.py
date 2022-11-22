# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'
    _description = 'Product Pricelist'

    is_allowed = fields.Boolean(string="Lista por defecto en contactos")