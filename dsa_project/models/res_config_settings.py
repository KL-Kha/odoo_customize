# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    use_mail_notify = fields.Boolean(
        'Task Notifications',
        help="Send email to Assignee when the task assigned to")

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'project.task.use_mail_notify', self.use_mail_notify)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        use_mail_notify = self.env['ir.config_parameter'].sudo()\
            .get_param('project.task.use_mail_notify') or False
        res.update(
            use_mail_notify=use_mail_notify
        )
        return res
