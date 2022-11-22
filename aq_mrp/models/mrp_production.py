# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    _description = 'Mrp Production'

    type_turn = fields.Selection([
        ('first', 'Primer turno'),
        ('second', 'Segundo turno'),
        ('third', 'Tercer turno')],
        string="Turno encargado")

    def action_confirm(self):
        for rec in self:
            if not rec.type_turn:
                raise ValidationError(_("Es necesario definir el turno encargado para esta orden de producción."))
        return super(MrpProduction, self).action_confirm()