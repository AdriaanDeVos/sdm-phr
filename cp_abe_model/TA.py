from charm.toolbox.pairinggroup import PairingGroup
from ABE.bsw07 import BSW07
from phr_repo import PHRRepo
from Role import ROLE
from User import UserClass

# Trusted Authority Class
class TA:
    """
    Trusted Authority Wrapper on the CP-ABE library.
    Initializes the private variables of this class.
    Provides various functions for setup/encryption/decryption.
    """
    __pairing_group = PairingGroup('MNT224')
    __cpabe = BSW07(__pairing_group, 2)
    (__pk, __msk) = __cpabe.setup()

    __file_server = PHRRepo()
    __attr_list = ['PATIENT', 'HOSPITAL', 'HEALTH_CLUB', 'DOCTOR', 'INSURANCE', 'EMPLOYER']
    __user_list = {}

    def __keygen(self, user_id):
        """
        Generate a key based on the set of attributes from a specific user.
        :param user_id: An identifier for the user.
        :return: An attribute list, master key and subkeys.
        """
        return self.__cpabe.keygen(self.__pk, self.__msk, self.__user_list[user_id][1])

    def __id_check(self, user_id):
        """
        Checks if a user with this specific identifier exists.
        :param user_id: The user identifier to check
        :return: True/false if it exists.
        """
        return user_id in self.__user_list.keys()

    def add_new_user(self, admin_id, role):
        """
        The user admin account with id -1 is able to add new users with different roles.
        For new patients an additional attribute needs to be added too.
        :param admin_id: The admin account has user_id -1.
        :param role: The role of this user.
        :return: The user identifier of the created user.
        """
        if admin_id != -1:
            print("[ERROR] Non-admin tried to create a new user.")
            return

        user_id = len(self.__user_list)
        user = UserClass(user_id, role, self, self.__file_server)
        user_attributes = []
        if role is ROLE.PATIENT:
            related = 'RELATED-TO-' + str(user_id)
            user_attributes = ['PATIENT', related]
            self.__attr_list.append(related)
        elif role is ROLE.HOSPITAL:
            user_attributes = ['HOSPITAL']
        elif role is ROLE.HEALTHCLUB:
            user_attributes = ['HEALTHCLUB']
        elif role is ROLE.DOCTOR:
            user_attributes = ['DOCTOR']
        elif role is ROLE.INSURANCE:
            user_attributes = ['INSURANCE']
        elif role is ROLE.EMPLOYER:
            user_attributes = ['EMPLOYER']

        self.__user_list[user_id] = [user, user_attributes]
        user.request_new_key()
        return user

    def add_related_to_patient(self, patient_id, target_user_id):
        """
        Provides functionality to add the `related_to_patient` permission to users.
        If the patient goes to a new doctor, he has to make sure this new doctor can read his records.
        :param patient_id: The user_id of the patient.
        :param target_user_id: The user_id of the doctor/insurance/employer.
        :return: True/False if it worked.
        """
        patient = self.__user_list[patient_id][1]
        attribute = 'RELATED-TO-' + str(patient_id)
        if 'PATIENT' in patient and attribute in self.__attr_list:
            user = self.__user_list[target_user_id][1]
            if 'DOCTOR' in user or 'INSURANCE' in user or 'EMPLOYER' in user:
                user.append(attribute)
                self.__user_list[target_user_id][0].request_new_key()
                return True
            print("[ERROR] User is not eligible to receive this permission with id: " + str(target_user_id))
        print("[ERROR] Patient not found in user list with id: " + patient_id)
        return False

    # TODO: Add ID check to prevent malicious key requests
    def key_request(self, user_id):
        """
        Generates and returns the key information for a specific user identifier.
        :param user_id: The user identifier that requests the information.
        :return: Attribute list, master key and subkeys, -1 if user doesnt exist.
        """
        if self.__id_check(user_id):
            return self.__keygen(user_id)
        else:
            return -1

    def get_pk(self):
        """
        Get the public key.
        :return: The public key.
        """
        return self.__pk

    def get_attributes(self):
        """
        Get a list of all possible attributes.
        :return: A list of all possible attributes.
        """
        return self.__attr_list
