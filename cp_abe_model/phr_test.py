import unittest
from TA import TA
import time


class TestTA(unittest.TestCase):

    def setUp(self):
        self.ta = TA()

    def test_download_entire_user(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        user0.encrypt_and_send(user0.get_user_id(), message, policy)
        collect = user0.file_server.download_entire_user(user0.get_user_id())
        self.assertTrue(type(collect) == dict)
        self.assertTrue(len(collect) == 1)

    def test_invalid_download_entire_user(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        user0.encrypt_and_send(user0.get_user_id(), message, policy)
        collect = user0.file_server.download_entire_user(10)
        self.assertTrue(type(collect) == dict)
        self.assertTrue(len(collect) == 0)

    def test_upload_file(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")

    def test_invalid_upload_file(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user3 = users[3]
        upload_return = user3.encrypt_and_send(users[0].get_user_id(), message, policy)
        self.assertTrue(upload_return is "")

    def test_replace_file(self):
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

    def test_invalid_replace_file(self):
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

    def test_get_ids_from_user(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        message2 = "dehondbijtdekat"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        first_upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(first_upload_return is not "")
        time.sleep(2)
        second_upload_return = user0.encrypt_and_send(user0.get_user_id(), message2, policy)
        self.assertTrue(second_upload_return is not "")
        user_file_ids = user0.file_server.get_ids_from_user(user0.get_user_id())
        self.assertTrue(type(user_file_ids) is list)

    def test_invalid_get_ids_from_user(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        message2 = "dehondbijtdekat"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        user_file_ids = user0.file_server.get_ids_from_user(100)
        self.assertTrue(type(user_file_ids) is list)
        self.assertTrue(len(user_file_ids) == 0)

    def test_download_single_record(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = user0.decrypt_from_send(upload_return)
        self.assertTrue(download_return == message)

    def test_invalid_download_single_record(self):
        policy = '(RELATED-TO-0 and PATIENT)'
        message = "dekatkraptdekrullenvandetrap"
        user_role_amount = [1, 1, 1, 1, 1, 1]
        users = self.ta.make_users(-1, user_role_amount)
        user0 = users[0]
        upload_return = user0.encrypt_and_send(user0.get_user_id(), message, policy)
        self.assertTrue(upload_return is not "")
        download_return = users[3].decrypt_from_send(upload_return)
        self.assertTrue(download_return is not message)


if __name__ == '__main__':
    unittest.main()
