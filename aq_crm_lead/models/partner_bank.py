# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    _description = 'Res Partner Bank'

    lead_id = fields.Many2one('crm.lead', string="Lead")