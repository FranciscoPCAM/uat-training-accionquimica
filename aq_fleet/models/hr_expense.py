# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class HrExpense(models.Model):
    _inherit = 'hr.expense'
    _description = 'HR Expense'

    expense_ref = fields.Char(string="Referencia del gasto")
    