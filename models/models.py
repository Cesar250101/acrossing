# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Productos(models.Model):
    _inherit = 'product.template'

    variable1= fields.Many2one(
        comodel_name='acrossing.variable1',
        string='Variable #1',
        required=False)
    variable2 = fields.Many2one(
        comodel_name='acrossing.variable2',
        string='Variable #2',
        required=False)
    marca = fields.Many2one(
        comodel_name='acrossing.marca_producto',
        string='Marca del Producto',
        required=False)

class Marcas(models.Model):
    _name = 'acrossing.marca_producto'

    name = fields.Char()

class Marcas(models.Model):
    _name = 'acrossing.variable1'

    name = fields.Char()


class Marcas(models.Model):
    _name = 'acrossing.variable2'

    name = fields.Char()

