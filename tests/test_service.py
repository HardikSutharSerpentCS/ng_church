from odoo.tests.common import TransactionCase



class TestServices(TransactionCase):

    def setUp(self):
        super(TestServices, self).setUp()

    def test(self):
        services_obj = self.env['ng_church.program']

        self.services = services_obj.create({
                                'name':'prayer',
                                'days':'Monday',
                                'start':'10.00',
                                'end':'10.30',
                                })