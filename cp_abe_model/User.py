import hashlib
from charm.toolbox.pairinggroup import PairingGroup, GT
from ABE.bsw07 import BSW07
from Crypto.Cipher import AES


class UserClass:
    __pairing_group = PairingGroup('MNT224')
    __cpabe = BSW07(__pairing_group, 2)

    def __init__(self, user_id, role, ta, fs):
        """
            Initialize the User object
            :param user_id: An identifier for the user.
            :param role: An enum for the role of theuser.
            :param ta: The trusted authority the user.
            :param fs: The fileserver of the user.
        """
        self.__user_id = user_id
        self.__role = role
        self.__ta = ta
        self.__public_key = ta.get_pk()
        self.__user_key = ta.key_request(user_id)
        self.__file_server = fs

    def __encrypt_message(self, message, policy):
        random_group_element = self.__pairing_group.random(GT)
        encrypt_aes_key = hashlib.sha256(str(random_group_element).encode('utf-8')).digest()
        encrypted_group_element = self.__cpabe.encrypt(self.__public_key, random_group_element, policy)
        cipher = AES.new(encrypt_aes_key)
        ciphertext = cipher.encrypt(self.__pad_message(message))
        return encrypted_group_element, ciphertext

    def __decrypt_message(self, abe_cipher, aes_cipher):
        decrypted_group_element = self.__cpabe.decrypt(self.__public_key, abe_cipher, self.__user_key)
        decrypt_aes_key = hashlib.sha256(str(decrypted_group_element).encode('utf-8')).digest()
        plaintext = AES.new(decrypt_aes_key).decrypt(aes_cipher).decode("utf-8")
        return self.__remove_padding(plaintext)

    def encrypt_and_send(self, user_id, message, policy):
        ct_elem, ct = self.__encrypt_message(message, policy)
        return self.__file_server.upload_file(user_id, ct_elem, ct)

    def decrypt_from_send(self, upload_id):
        health_record = self.__file_server.download_single_record(upload_id)
        return self.__decrypt_message(health_record['abe'], health_record['aes'])

    def get_user_id(self):
        """
            Get user_id.
            :return: An int representing the id of the user.
        """
        return self.__user_id

    def get_role(self):
        """
            Get role.
            :return: An enum representing the role of the user.
        """
        return self.__role

    def __pad_message(self, msg):
        spare_length = len(msg) % 16
        return msg + ("~" * (16 - spare_length))

    def __remove_padding(self, msg):
        return msg[:-16] + msg[-16:].replace('~', '')
