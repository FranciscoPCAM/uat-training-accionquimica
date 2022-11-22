# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MaintenanceCriticality(models.Model):
    _name = 'maintenance.criticality'
    _description = 'Maintenance Criticality'

    name = fields.Char(string='Tipo')