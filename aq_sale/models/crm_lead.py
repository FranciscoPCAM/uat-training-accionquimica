# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class CustomLeads(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead'

    partner_button = fields.Char(string="Cliente", related='partner_id.name')

    def partner_button_action(self):
        """ 
        Opens a new partner view in readonly mode

        """
        action = self.env.ref('aq_sale.action_partner_customer')
        result = action.read()[0]
        res = self.env.ref('base.view_partner_form', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['res_id'] = self.partner_id.id
        return result