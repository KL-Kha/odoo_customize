# -*- coding: utf-8 -*-

from odoo import api, models, _


class Task(models.Model):
    _inherit = "project.task"

    def _task_message_auto_subscribe_notify(self, users_per_task):
        use_mail_notify = self.env['ir.config_parameter'].sudo()\
            .get_param('project.task.use_mail_notify') or False
        if use_mail_notify:
            super(Task, self)._task_message_auto_subscribe_notify(users_per_task)
