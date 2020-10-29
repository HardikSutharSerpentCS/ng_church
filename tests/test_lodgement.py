from odoo.tests.common import TransactionCase
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT


class TestLodgement(TransactionCase):

    def setUp(self):
        super(TestLodgement, self).setUp()

    def test(self):
        lodgement_obj = self.env['ng_church.lodgement']
        journal_id = self.env['account.journal'].create({
                                                    'name':'Bank',
                                                    'type':'bank',
                                                    'code':'bank',
                                                    })
        cr_dt = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        self.pledge = lodgement_obj.create({
                                        'journal_id':journal_id.id,
                                        'date':cr_dt,
                                        'amount':1000,
                                        'description':'For Help',
                                        })