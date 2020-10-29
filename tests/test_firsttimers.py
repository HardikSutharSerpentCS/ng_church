from odoo.tests.common import TransactionCase


class TestFirstTimers(TransactionCase):

    def setUp(self):
        super(TestFirstTimers, self).setUp()

    def test(self):
        first_timers_obj = self.env['res.partner']

        self.first_timers = first_timers_obj.create({
                                        'name':'Felix',
                                        'phone':9989989989,
                                        'email':'abc@gmail.com',
                                        'street':'Gandhinagar',
                                        })