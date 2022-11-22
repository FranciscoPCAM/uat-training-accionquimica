# -*- coding: utf-8 -*-

# import logging

# from odoo import _, api, fields, models

# _logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'
    _description = 'purchase customization'

    confidential_vendor = fields.Boolean(string="Proveedor confidencial",related="partner_id.confidential_vendor")
    partner_button = fields.Char(string="Proveedor", related='partner_id.name')
    confidential_vendor = fields.Boolean(string="Proveedor confidencial", related='partner_id.confidential_vendor')

    def partner_button_action(self):
        """ 
        Opens a new partner view in readonly mode

        """
        action = self.env.ref('aq_purchase.action_visualizer_supplier')
        result = action.read()[0]
        res = self.env.ref('base.view_partner_form', False)
        result['views'] = [(res and res.id or False, 'form')]
        result['res_id'] = self.partner_id.id
        return result