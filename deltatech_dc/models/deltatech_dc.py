# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
# See README.rst file on addons root folder for license details


from openerp import models, fields, api, _


class deltatech_dc(models.Model):
    _name = 'deltatech.dc'
    _description = "Declaration of Conformity"

    name = fields.Char('Number', size=32, required=True, )
    date = fields.Date('Date of Declaration', required=True, )
    product_id = fields.Many2one('product.product', 'Product', required=True, select=True,
                                 domain=[('sale_ok', '=', 'True')])
    company_standard = fields.Char(related='product_id.company_standard', string="Standard of Company",
                                   store=False)
    data_sheet = fields.Integer(related='product_id.data_sheet', string="Data Sheet", store=False)
    technical_specification = fields.Integer(related='product_id.technical_specification', string="Technical Specification",
                                             store=False)
    standards = fields.Text(related='product_id.standards', string="Standards", store=False)

    @api.multi
    def name_get(self):
        result = []
        for line in self:
            name = (line.product_id.name or '') + ' (' + (line.name or '') + '/' + (line.date or '') + ')'
            result.append((line.id, name))

        return result