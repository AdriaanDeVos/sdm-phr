from charm.toolbox.pairinggroup import PairingGroup, GT
from ABE.bsw07 import BSW07

# Trusted Authority Class
class TAClass:
    # Hardcoded init
    __pairing_group = PairingGroup('MNT224')
    __cpabe = BSW07(__pairing_group, 2)
    (__pk, msk) = __cpabe.setup()
    __files = {}

    # Variable init
    def __init__(self, attr_list, user_list):
        self.__attr_list = attr_list
        self.__user_list = user_list

    # Key creation for user class
    def __keygen(self, user_id):
        return self.__cpabe.keygen(self.__pk, self.msk, self.__user_list[user_id])

    def get_pk(self):
        return self.__pk

    def get_attributes(self):
        return self.__attr_list

    # TODO MAG DEZE NAAR DE USERS?!!??
    def get_cp_abe(self):
        return self.__cpabe

    def get_file(self, file_id):
        if file_id in self.__files.keys():
            return self.__files[file_id]
        else:
            return -1

    def get_file_ids(self):
        return self.__files.keys()

    # TODO This allows for malicious uploads
    def upload_file(self, file_id, file):
        self.__files[file_id] = file
        return

    # TODO: This allows for malicious key requests
    def key_request(self, user_id):
        if self.id_check(user_id):
            return self.__keygen(user_id)
        else:
            return -1

    def id_check(self, user_id):
        return user_id in self.__user_list.keys()
