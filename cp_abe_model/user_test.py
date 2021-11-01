import unittest
from TA import TA
from Role import ROLE


class TestTA(unittest.TestCase):

    def setUp(self):
        self.ta = TA()

    def test_get_attributes(self):
        self.ta = TA()
        attr_list = ['PATIENT', 'HOSPITAL', 'HEALTH_CLUB', 'DOCTOR', 'INSURANCE', 'EMPLOYER']
        result = self.ta.get_attributes()
        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 6)

    def test_add_user(self):
        self.ta.add_new_user(-1, ROLE(0))
        key = self.ta.key_request(0)
        self.assertIsNotNone(key)
        self.assertTrue(type(key) is dict)

    def test_user_init_length(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        self.assertEqual(len(users), 6)

    def test_user_init_role(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        for i in range(len(users)):
            self.assertTrue(users[i].get_role(), ROLE(i))

    def test_user_init_id(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        for i in range(len(users)):
            self.assertTrue(users[i].get_role(), i)

    def test_related_to_patient_doctor(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        self.assertTrue(self.ta.add_related_to_patient(0, 3))

    def test_related_to_patient_insurance(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        self.assertTrue(self.ta.add_related_to_patient(0, 4))

    def test_related_to_patient_employer(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        self.assertTrue(self.ta.add_related_to_patient(0, 5))

    def test_invalid_related_to_patient(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        self.assertFalse(self.ta.add_related_to_patient(3, 1))

    def test_key_request(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        key = self.ta.key_request(0)
        self.assertIsNotNone(key)
        self.assertTrue(type(key) is dict)

    def test_invalid_key_request(self):
        key = self.ta.key_request(0)
        self.assertIsNotNone(key)
        self.assertIs(key, -1)

    def test_get_pk(self):
        pk = self.ta.get_pk()
        self.assertIsNotNone(pk)
        self.assertTrue(type(pk) is dict)

    def test_get_attributes_add_patient(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        attr_list = ['PATIENT', 'HOSPITAL', 'HEALTH_CLUB', 'DOCTOR', 'INSURANCE', 'EMPLOYER', 'RELATED-TO-0']
        self.assertTrue(self.ta.get_attributes() == attr_list)


if __name__ == '__main__':
    unittest.main()
