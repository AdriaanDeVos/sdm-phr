from charm.toolbox.pairinggroup import PairingGroup, GT
from ABE.bsw07 import BSW07


class TAClass:
    # Hardcoded init
    __pairing_group = PairingGroup('MNT224')
    __cpabe = BSW07(__pairing_group, 2)
    (__pk, msk) = __cpabe.setup()

    # Variable init
    def __init__(self, attr_list, user_list):
        self.__attr_list = attr_list
        self.__user_list = user_list

    def __keygen(self, user_id):
        return self.__cpabe.keygen(self.__pk, self.msk, self.__user_list[user_id])

    def get_pk(self):
        return self.__pk

    def get_attributes(self):
        return self.__attr_list

    # TODO MAG DEZE NAAR DE USERS?!!??
    def get_cp_abe(self):
        return self.__cpabe

    # TODO
    def get_file(self, file_id):
        return

    # TODO
    def upload_file(self, file):
        return

    def key_request(self, user_id):
        if self.id_check(user_id):
            return self.__keygen(user_id)
        else:
            return -1

    def id_check(self, user_id):
        return user_id in self.__user_list.keys()
