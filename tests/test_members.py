from odoo.tests.common import TransactionCase


class TestMembers(TransactionCase):

    def setUp(self):
        super(TestMembers, self).setUp()

    def test(self):
        members_obj = self.env['res.partner']

        self.members = members_obj.create({
                                    'name':'Felix',
                                    'phone':9989989989,
                                    'email':'abc@gmail.com',
                                    'street':'Gandhinagar',
                                    })