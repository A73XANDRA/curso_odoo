from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Is Teacher')
    is_freelance = fields.Boolean(string='Is Freelance')
    is_student = fields.Boolean(string='Is Student')
    vat = fields.Char(required=True, copy=False) 

    def unlink(self):
        for partner in self:
            if partner.email == 'maintecaher@gmail.com':
                courses = self.env['grades.course'].search([('teacher_id', '=', self.id)])
                secondary_teacher = self.env['res.partner'].search([('email', '=', 'mail@secundario.com')])
                courses.write({'teacher_id': secondary_teacher.id})
        result = super(ResPartner, self).unlink()
        return result

    def copy(self, default=None):
        default = default or {}
        if self.is_teacher:
            default['name'] = 'Teacher'
        elif self.is_student:
            default['name'] = 'Student'
        res = super(ResPartner,self).copy(default)
        return  res