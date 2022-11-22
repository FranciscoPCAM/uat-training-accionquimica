# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'
    _description = 'Account Payment Term'

    is_default = fields.Boolean(string="Valor por defecto?")