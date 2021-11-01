import unittest
from TA import TA
from Role import ROLE


class TestTA(unittest.TestCase):

    def setUp(self):
        self.ta = TA()

    def test_get_role(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        for i in range(len(users)):
            self.assertTrue(users[i].get_role(), ROLE(i))

    def test_user_init_id(self):
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        for i in range(len(users)):
            self.assertTrue(users[i].get_role(), i)

    def test_encrypt_and_send(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")

    def test_invalid_encrypt_and_send(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user3 = users[3]
        upload_return = user3.encrypt_and_send(users[0].get_user_id(), message, policy)
        self.assertTrue(upload_return is "")

    def test_decrypt_from_send(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)

    def test_invalid_decrypt_from_send(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = users[3].decrypt_from_send(upload_return)
        self.assertTrue(download_return is not message)

    def test_padding(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekat"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)

    def test_replace(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        new_policy = '(RELATED-TO-0 and (PATIENT or DOCTOR))'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        self.ta.add_related_to_patient(user0.get_user_id(), users[3].get_user_id())
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)
        replace_return = user0.replace(upload_return, new_policy)
        self.assertTrue(replace_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)
        download_return = users[3].decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)

    def test_invalid_replace(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        new_policy = '(RELATED-TO-0 and (PATIENT or INSURANCE))'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        self.ta.add_related_to_patient(user0.get_user_id(), users[3].get_user_id())
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)
        replace_return = user0.replace(upload_return, new_policy)
        self.assertTrue(replace_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)
        download_return = users[3].decrypt_from_send(upload_return)
        self.assertTrue(download_return is not message)

if __name__ == '__main__':
    unittest.main()
