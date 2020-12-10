# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Productos(models.Model):
    _inherit = 'product.template'

    variable1 = fields.Char(
        string='Variable n°1',
        required=False)
    variable2 = fields.Char(
        string='Variable n°2',
        required=False)

