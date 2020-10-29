from odoo.tests.common import TransactionCase


class TestChurch(TransactionCase):

    def setUp(self):
        super(TestChurch, self).setUp()

    def test(self):
        church_obj = self.env['res.company']
        currency_id = self.env['res.company']

        self.church = church_obj.create({
                                'name':'st.xaviers',
                                'phone':99899899811,
                                'email':'abc@gmail.com',
                                'street':'Gandhinagar',
                                })