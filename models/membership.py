# -*- coding: utf-8 -*-
"""."""

from odoo import fields, models, api, _
import re

DATETIME_FORMAT = "%Y-%m-%d"


class Associate(models.Model):
    """Church Associate Model."""

    _name = 'ng_church.associate'
    _description = "Ng Church Associate"

    name = fields.Char(string='Full Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')


class ChurchGuarantor(models.Model):
    """Church Guarantor Model."""

    _name = 'church.guarantor'
    _description = "Church Guarantor"

    name = fields.Char(string='First Name', required=True)
    lname = fields.Char(string='Last Name', required=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string='Gender', required=False)
    marital = fields.Selection([('single', 'Single'), ('married', 'Married'),
                                ('widower', 'Widower'),
                                ('divorced', 'Divorced')],
                               string='Marital Status', required=False)
    home = fields.Text(string='Home Address', required=False)
    office = fields.Text(string='Office Address', required=False)
    email = fields.Char(string='Email')
    tel1 = fields.Char(string='Telephone Number 1', required=False)
    tel2 = fields.Char(string='Telephone Number 2', required=False)
    rel = fields.Char(string='Relationship with Employee', required=False)
    status = fields.Selection([('e', 'Employed'), ('s', ' Self Employed'),
                               ('u', 'Unemployed')], string='Work Status',
                              required=False)
    state = fields.Selection(selection=[
        ('not_verify', 'Not Verified'),
        ('verify', 'Verified'),
        ('declined', 'Declined')],
        string='Status', readonly=False, required=True, default='not_verify')
    employer = fields.Char(string='Employer')
    notes = fields.Text(string='Notes')
    emp_id = fields.Many2one('res.partner', string='Employee')

    @api.constrains('email')
    def _check_email(self):
        email_re = re.compile(r"""
        ([a-zA-Z][\w\.-]*[a-zA-Z0-9]     # username part
        @                                # mandatory @ sign
        [a-zA-Z0-9][\w\.-]*              # domain must start with a letter
         \.
         [a-z]{2,3}                      # TLD
        )
        """, re.VERBOSE)
        for guarantor in self:
            if guarantor.email:
                if not email_re.match(guarantor.email):
                    raise Warning(_('Warning'), _('Please enter valid'
                                                  ' email address'))


class ChurchNextofkin(models.Model):
    """Church Nextofkin Model."""

    _name = 'church.nextofkin'
    _description = "Church Nextofkin"

    name = fields.Char(string='First Name', required=True)
    lname = fields.Char(string='Last Name', required=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              'Gender', required=False)
    marital = fields.Selection([('single', 'Single'), ('married', 'Married'),
                                ('widower', 'Widower'),
                                ('divorced', 'Divorced')],
                               'Marital Status', required=False)
    home = fields.Text(string='Home Address', required=False)
    office = fields.Text(string='Office Address', required=False)
    email = fields.Char(string='Email')
    tel1 = fields.Char(string='Telephone Number 1', required=False)
    tel2 = fields.Char(string='Telephone Number 2', required=False)
    rel = fields.Char(string='Relationship with Employee', required=False)
    status = fields.Selection([('e', 'Employed'), ('s', ' Self Employed'),
                               ('u', 'Unemployed')], 'Status', required=False)
    employer = fields.Char(string='Employer')
    notes = fields.Text(string='Notes')
    emp_id = fields.Many2one('res.partner', string='Employee')

    @api.constrains('email')
    def _check_email(self):
        email_re = re.compile(r"""
        ([a-zA-Z][\w\.-]*[a-zA-Z0-9]     # username part
        @                                # mandatory @ sign
        [a-zA-Z0-9][\w\.-]*              # domain must start with a letter
         \.
         [a-z]{2,3}                      # TLD
        )
        """, re.VERBOSE)
        for nextofkin in self:
            if nextofkin.email:
                if not email_re.match(nextofkin.email):
                    raise Warning(_('Warning'), _(
                        'Please enter valid email address'))


class ChurchRef(models.Model):
    """Church Reference model."""

    _name = 'church.refs'
    _description = "Church Refs"

    name = fields.Char(string='First Name', required=True)
    lname = fields.Char(string='Last Name', required=False)
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')],
                              string='Gender', required=False)
    marital = fields.Selection(selection=[('single', 'Single'),
                                          ('married', 'Married'), (
        'widower', 'Widower'), ('divorced', 'Divorced')],
        string='Marital Status', required=False)
    home = fields.Text(string='Home Address', required=False)
    office = fields.Text(string='Office Address', required=False)
    email = fields.Char(string='Email')
    tel1 = fields.Char(string='Telephone Number 1', required=False)
    tel2 = fields.Char(string='Telephone Number 2', required=False)
    rel = fields.Char(string='Relationship with Employee', required=False)
    status = fields.Selection(
        selection=[('e', 'Employed'), ('s', ' Self Employed'),
                   ('u', 'Unemployed')], string='Work Status', required=False)
    state = fields.Selection(selection=[
        ('not_verify', 'Not Verified'),
        ('verify', 'Verified')],
        string='Status', default='not_verify', readonly=True)
    user = fields.Many2one('res.users', string='Verified By',
                           required=False, readonly=True)
    employer = fields.Char('Employer')
    notes = fields.Text('Notes')
    emp_id = fields.Many2one('res.partner', string='Employee')

    def verify(self):
        """Method to update status."""
        return self.write({'state': 'verify', 'user': self._uid})

    def notverify(self):
        """Method to update status."""
        return self.write({'state': 'not_verify', 'user': self._uid})

    @api.constrains('email')
    def _check_email(self):
        email_re = re.compile(r"""
        ([a-zA-Z][\w\.-]*[a-zA-Z0-9]     # username part
        @                                # mandatory @ sign
        [a-zA-Z0-9][\w\.-]*              # domain must start with a letter
         \.
         [a-z]{2,3}                      # TLD
        )
        """, re.VERBOSE)
        for church_ref in self:
            if church_ref.email:
                if not email_re.match(church_ref.email):
                    raise Warning(_('Warning'), _('Please enter a'
                                                  ' valid email address'))
