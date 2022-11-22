# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Leads(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead'

    customer_class = fields.Selection([
        ('consu', 'Consumidor'),
        ('comer', 'Comercializador')],
        string="Clasificación de cliente",
        required=1)
    product_ids = fields.Many2many('product.product',
        string="Productos solicitados",
        required=1, 
        domain=[('sale_ok', '=', 1)])
    vat = fields.Char(string="RFC", required=1)
    bank_ids = fields.One2many('res.partner.bank', 'lead_id', 
        string='Bancos',
        required=1)
    type_lead = fields.Selection([
        ('old', 'Cliente recurrente'),
        ('new', 'Nueva venta')],
        string="Tipo de lead")

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        """ Extends for new data syncronization.

        """
        res = super(Leads, self)._prepare_customer_values(partner_name, is_company, parent_id)

        res['customer_rank'] = 1
        res['vat'] = self.vat if self.vat else ''
        res['customer_class'] = self.customer_class if self.customer_class else 'consu'
        if not res.get('parent_id') or False:
            res['bank_ids'] = [(6,0,self.bank_ids.ids)] if self.bank_ids else False
        
        return res

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            if rec.partner_id:
                sale_order = self.env['sale.order'].search([('partner_id','=',rec.partner_id.id)])
                if sale_order:
                    rec.type_lead = 'old'
                else:
                    rec.type_lead = 'new'
                # Uncomment if needed:
                rec.vat = rec.partner_id.vat
                rec.customer_class = rec.partner_id.customer_class

    @api.model
    def create(self, vals):
        res = super(Leads, self).create(vals)
        for rec in res:
            if rec.partner_id and not rec.type_lead:
                sale_order = self.env['sale.order'].search([('partner_id','=',rec.partner_id.id)])
                if sale_order:
                    rec.type_lead = 'old'
                else:
                    rec.type_lead = 'new'

                rec.vat = rec.partner_id.vat
                rec.customer_class = rec.partner_id.customer_class
        return res

    def write(self, vals):
        res = super(Leads, self).write(vals)
        for rec in self:
            if rec.partner_id and not rec.type_lead:
                sale_order = self.env['sale.order'].search([('partner_id','=',rec.partner_id.id)])
                if sale_order:
                    rec.type_lead = 'old'
                else:
                    rec.type_lead = 'new'
                    
                rec.vat = rec.partner_id.vat
                rec.customer_class = rec.partner_id.customer_class
        return res