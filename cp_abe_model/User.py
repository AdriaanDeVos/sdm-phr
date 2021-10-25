import hashlib
from charm.toolbox.pairinggroup import PairingGroup, GT
from ABE.bsw07 import BSW07
from Crypto.Cipher import AES


class UserClass:
    pairing_group = PairingGroup('MNT224')
    cpabe = BSW07(pairing_group, 2)

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
        self.__user_key = ta.key_request(user_id)
        self.__file_server = fs

    # TODO
    def __encrypt_message(self):
        return

    # TODO
    def __decrypt_message(self):
        return

    def encrypt_and_send(self, message, policy):
        # TODO encrypt message
        # TODO send to FS
        # TODO return success or error
        return

    def decrypt_and_send(self, message_id):
        # TODO obtain the msaage message_if from fs
        # TODO call decrypt_message function
        # TODO return result
        return

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
