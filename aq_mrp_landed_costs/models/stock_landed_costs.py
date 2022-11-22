# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockLandedCosts(models.Model):
    _inherit = 'stock.landed.cost'
    _description = 'Stock Landed Costs'

    @api.model
    def default_get(self, fields_list):
        res = super(StockLandedCosts, self).default_get(fields_list)
        vals = []
        product_obj = self.env['product.product'].search([('landed_cost_ok', '=', True)])
        for product in product_obj:
            product_row = (0, 0, {'product_id': product.id,
                    'price_unit': 0.00,
                    'split_method': product.split_method_landed_cost or 'equal'})
            vals.append(product_row)
        res.update({'cost_lines': vals})
        return res