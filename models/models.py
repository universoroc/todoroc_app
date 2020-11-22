# -*- coding: utf-8 -*-
""" TODO: Modelo de la aplicacion """

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class todoroc_app(models.Model):
    """TODO: model del proyecto -- tareas por hacer del usuario """

    _name = 'todoroc_app.todoroc_app'
    _description = 'To-do Task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    # FIXME: hace falta verificar
    def todo_app_do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    # OPTIMIZE: hace falta optimizar
    def todo_app_do_clear_done(self):
        dones = self.search([('is_done', '=', True)])
        dones.write({'is_done': False})
        return True

    def todo_app_do_active(self):
        dones = self.search([('is_done', '=', True)])
        self.active = True
        dones.write({'active': True})
        return True

