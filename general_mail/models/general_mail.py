from odoo import api, fields, models


class GeneralMail(models.Model):
    _name = 'general.mail'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'General Mail'

    name = fields.Char(default="Activity")


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    @api.onchange('activity_type_id','hiring_id')
    def general_mail(self):
        if not (self.res_id and self.res_model_id and self.hiring_id):
            self.res_id = 1
            self.res_model_id = self.env['ir.model'].search([('model', '=', 'general.mail')], limit=1).id
