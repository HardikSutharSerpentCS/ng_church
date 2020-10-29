from odoo.tests.common import TransactionCase
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT


class TestDonation(TransactionCase):

    def setUp(self):
        super(TestDonation, self).setUp()

    def test(self):
        donation_obj = self.env['ng_church.donation']
        project_id = self.env['project.project'].create({'name':'Research & Development'})
        cr_dt = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        donation_line_obj = self.env['ng_church.donation_line']

        self.donation_line = donation_line_obj.create({
                                                'date':cr_dt,
                                                'amount':1000
                                                })

        self.donation = donation_obj.create({
                                        'name':project_id.id,
                                        'start_date':cr_dt,
                                        'donation_line_ids':self.donation_line
                                        })