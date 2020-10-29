from odoo.tests.common import TransactionCase
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT

class TestOffering(TransactionCase):

    def setUp(self):
        super(TestOffering, self).setUp()

    def test(self):
        offering_obj = self.env['ng_church.offering']
        collection_id = self.env['ng_church.collection']
        section_id = self.env['church.sections'].create({'name':'Children Church'})
        service_id = self.env['ng_church.program']
        offering_line_obj = self.env['ng_church.offering_line']
        cr_dt = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        self.offering_line = offering_line_obj.create({
                                                'date':cr_dt,
                                                'amount':1000

                                                })

        self.offering = offering_obj.create({
                                    'name':collection_id.id,
                                    'section_id':section_id.id,
                                    'service_id':service_id.id,
                                    'offering_line_ids':self.offering_line
                                    })