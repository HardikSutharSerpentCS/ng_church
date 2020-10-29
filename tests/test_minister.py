from odoo.tests.common import TransactionCase


class TestMinister(TransactionCase):

    def setUp(self):
        super(TestMinister, self).setUp()

    def test(self):
        minister_obj = self.env['ng_church.pastor']
        user_id = self.env['res.users']
        church_id = self.env['res.company']

        self.minister = minister_obj.create({
                                    'name':'Felix',
                                    'lastname':'xavier',
                                    'minister_hierarchy':'minister',
                                    'church_id':church_id.id,
                                    'personal_email':'felixxavier@gmail.com',
                                    })