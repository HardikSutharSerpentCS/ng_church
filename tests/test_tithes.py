from odoo.tests.common import TransactionCase
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT

class TestTithes(TransactionCase):

    def setUp(self):
        super(TestTithes, self).setUp()

    def test(self):
        tithes_obj = self.env['ng_church.tithe']
        collection_id = self.env['ng_church.collection']
        section_id = self.env['church.sections'].create({'name':'Children Church'})
        service_id = self.env['ng_church.program']
        tithes_line_obj = self.env['ng_church.tithe_lines']
        cr_dt = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        self.tithes_line = tithes_line_obj.create({
                                            'date':cr_dt,
                                            'tithe_type':'members',
                                            'amount':1000
                                            })

        self.tithes = tithes_obj.create({
                                    'name':collection_id.id,
                                    'section_id':section_id.id,
                                    'service_id':service_id.id,
                                    'tithe_line_ids':self.tithes_line
                                    })