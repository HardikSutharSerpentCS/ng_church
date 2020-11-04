# -*- coding: utf-8 -*-
"""."""

from odoo import api, fields, models


class PledgesReport(models.AbstractModel):
    """PledgesReport."""

    _name = 'report.ng_church.church_pledges_report'
    _description = "Report NG Church Church Pledges Report"

    def reports_presenter(self, model):
        """Mutate the state of the original report(s)."""
        return model

    # @api.model
    # def render_html(self, docids, data=None):
    #     """."""
    #     name = 'ng_church.church_pledges_report'
    #     report_obj = self.env['report']
    #     report = report_obj._get_report_from_name(name)
    #     docargs = {
    #         'doc_ids': docids,
    #         'doc_model': report.model,
    #         'docs': self.env['ng_church.pledge'].browse(docids),
    #         'presenter': self.reports_presenter
    #     }
    #     return report_obj.render(name, docargs)

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['ng_church.pledge'].browse(docids)
        return {
        'doc_ids': docs.ids,
        'doc_model': 'ng_church.pledge',
        'docs': self.env['ng_church.pledge'].browse(docids),
        }

class ChurchPledgeReport(models.TransientModel):
    """."""

    _name = 'ng_church.pledge_wizard'
    _description = "NG Church Pledge Wizard"

    pledge = fields.Many2one('ng_church.pledge', string="Pledge",
                             required=True)

    def check_report(self):
        """."""
        report = self.pledge.name.name
        pledges = self.env['ng_church.pledge'].search([('name', '=', report)])
        return self.env.ref('ng_church.ng_church_pledges_report').report_action(pledges)

