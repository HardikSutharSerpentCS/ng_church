from odoo.tests.common import TransactionCase
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT


class TestPledge(TransactionCase):

    def setUp(self):
        super(TestPledge, self).setUp()

    def test(self):
        pledge_obj = self.env['ng_church.pledge']
        project_id = self.env['project.project'].create({'name':'Research & Development'})
        cr_dt = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        pledge_line_obj = self.env['ng_church.pledge_line']
        pledge_associan_id = self.env['ng_church.associate'].create({'name':'Rutul Bhatt'})

        self.pledge_line = pledge_line_obj.create({
                                            'date':cr_dt,
                                            'pledger':pledge_associan_id.id,
                                            'amount':1000,
                                            })

        self.pledge = pledge_obj.create({
                                    'name':project_id.id,
                                    'date':cr_dt,
                                    'pledge_line_ids':self.pledge_line
                                    })