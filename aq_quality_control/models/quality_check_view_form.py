# -*- coding: utf-8 -*-

import logging
from ast import literal_eval

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class QualityCheck(models.Model):
    _inherit = 'quality.check'
    _description = 'Quality Check'

    is_blocked = fields.Boolean(string="Hoja bloqueada?")

    def do_fail(self):
        res = super(QualityCheck, self).do_fail()
        if not self.is_blocked:
            self.write({'is_blocked': True})

        return res

    def do_pass(self):
        res = super(QualityCheck, self).do_pass()
        if not self.is_blocked:
            self.write({'is_blocked': True})

        return res

    def action_quality_worksheet_readonly(self):
        action = self.worksheet_template_id.action_id.sudo().read()[0]
        worksheet = self.env[self.worksheet_template_id.model_id.sudo().model].search([('x_quality_check_id', '=', self.id)])
        context = literal_eval(action.get('context', '{}'))
        action.update({
            'res_id': worksheet.id if worksheet else False,
            'views': [(False, 'form')],
            'context': {
                **context,
                'edit': False, 
                'default_x_quality_check_id': self.id,
            },
        })
        return action