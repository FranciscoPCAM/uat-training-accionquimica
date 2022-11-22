# -*- coding: utf-8 -*-

# import logging

# from odoo import _, api, fields, models

# _logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class VendorRank(models.Model):
    _name = 'vendor.rank'
    _description = 'Vendor Rank'

    name = fields.Char(string="Nombre", required=1)