# -*- coding: utf-8 -*-

# import logging

# from odoo import _, api, fields, models

# _logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner customization'

    confidential_vendor = fields.Boolean(string="Proveedor confidencial")
    vendor_rank_ids = fields.Many2many('vendor.rank',string="Clasificación de proveedor")