# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'tareas.tareas'

    name = fields.Char()

class tarea(models.Model):
    _name = "tareas.tarea"
    _description = "tareas.tarea"
    
    nombre = fields.Char(string="Nombre", required=True, help="Introducir nombre")
    descripcion = fields.Text()
    horas = fields.Integer()
    fecha_creacion = fields.Date()
    fecha_comienzo = fields.Datetime()
    fecha_fin = fields.Datetime()
    pausada = fields.Boolean()

    sprint_id = fields.Many2one('tareas.sprint', string='Sprint')
    tecnologias_ids = fields.Many2many('tareas.tecnologia', string='Tecnologías')
    
class sprint(models.Model):
    _name = "tareas.sprint"
    _description = "tareas.sprint"
    
    nombre = fields.Char()
    descripcion = fields.Text()
    fecha_creacion = fields.Datetime()
    fecha_fin = fields.Datetime()

    tarea_ids = fields.One2many('tareas.tarea', 'sprint_id', string='Tareas')
    
class tecnologia(models.Model):
    _name = "tareas.tecnologia"
    _description = "tareas.tecnologia"
    
    nombre = fields.Char()
    foto = fields.Image(
        string = "Foto",
        max_width = 200,
        max_height = 200
    )
    