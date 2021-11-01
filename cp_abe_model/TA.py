from charm.toolbox.pairinggroup import PairingGroup
from ABE.bsw07 import BSW07

# Trusted Authority Class
class TAClass:
    """
    Trusted Authority Wrapper on the CP-ABE library.
    Initializes the private variables of this class.
    Provides various functions for setup/encryption/decryption.
    """
    __pairing_group = PairingGroup('MNT224')
    __cpabe = BSW07(__pairing_group, 2)
    (__pk, __msk) = __cpabe.setup()
    __files = {}

    # TODO Add new user (hospital/healthclub/insurer/etc)
    # TODO Allow a patient to give (related_to_patient) access to an employer/etc
    def __init__(self, attr_list, user_list):
        """
        Initializes the class based on given attribute and user lists.
        :param attr_list: A list containing all possible attributes.
        :param user_list: A nested list containing the attributes of a specific user.
        """
        self.__attr_list = attr_list
        self.__user_list = user_list

    def __keygen(self, user_id):
        """
        Generate a key based on the set of attributes from a specific user.
        :param user_id: An identifier for the user.
        :return: An attribute list, master key and subkeys.
        """
        return self.__cpabe.keygen(self.__pk, self.__msk, self.__user_list[user_id])

    def __id_check(self, user_id):
        """
        Checks if a user with this specific identifier exists.
        :param user_id: The user identifier to check
        :return: True/false if it exists.
        """
        return user_id in self.__user_list.keys()

    def add_related_to_patient(self, patient_id, user_id):
        """
        Provides functionality to add the `related_to_patient` permission to users.
        If the patient goes to a new doctor, he has to make sure this new doctor can read his records.
        :param patient_id: The user_id of the patient.
        :param user_id: The user_id of the doctor/insurance/employer.
        :return: True/False if it worked.
        """
        patient = self.__user_list[patient_id]
        attribute = 'RELATED-TO-' + str(patient_id)
        if 'PATIENT' in patient and attribute in self.__attr_list:
            user = self.__user_list[user_id]
            if 'DOCTOR' in user or 'INSURANCE' in user or 'EMPLOYER' in user:
                user.append(attribute)
                return True
            print("[ERROR] User is not eligible to receive this permission with id: " + patient_id)
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

    # TODO Add ID check to prevent malicious uploads
    def upload_file(self, file_id, file):
        """
        Saves the file content and identifier.
        :param file_id: An identifier for the uploaded file
        :param file: The content of the uploaded file
        """
        self.__files[file_id] = file

    def get_file(self, file_id):
        """
        Returns the content of a specific file identifier.
        If it doesnt exist, throw an error and return -1
        :param file_id: An identifier for the file.
        :return: The file content, or -1 if it doesnt exist.
        """
        if file_id in self.__files.keys():
            return self.__files[file_id]
        else:
            print("[ERROR] File not found with ID", file_id)
            return -1

    def get_file_ids(self):
        """
        Get a list of all uploaded file identifiers.
        :return: a list of all uploaded file identifiers.
        """
        return self.__files.keys()

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
