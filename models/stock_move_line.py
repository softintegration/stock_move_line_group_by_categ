# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    categ_id = fields.Many2one('product.category', 'Product Category',related='product_id.categ_id',store=True,
                               readonly=True)
