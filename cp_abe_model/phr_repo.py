import time


# Personal Health Record Repository Class
class PHRRepo:
    """
    Personal Health Record Repository Class that acts as a file server for
    the uploading and downloading of single records. In addition, you can
    request records_ids for a user, or downloading all records from an user.
    """
    __records = {}

    def __init__(self, TA):
        self.__ta = TA

    def upload_file(self, user_id, patient_id, abe_cipher, aes_cipher):
        """
        Upload a file and store the file in memory.
        Generate a record_id with a concat of the user and the unix timestamp
        Structure is: Dictionary with keys of userID containing
        dictionaries with keys of timestamps containing single records.
        {user_id: {timestamp: record}}
        :param user_id: The identifier of the patient.
        :param patient_id: The identifier of the
        :param abe_cipher: The output of abe_encrypt containing the encrypted group element.
        :param aes_cipher: The output of aes_encrypt containing the encrypted record content.
        :return: Return the record_id of the inserted record.
        """
        if self.__check_user_id(user_id) and self.__check_user_id(patient_id):
            if not self.__ta.can_user_do_upload(user_id, patient_id):
                print("[ERROR] User with id " + str(user_id) + " can not upload for patient: " + str(patient_id))
                return ""
            timestamp = int(time.time())
            if not self.__check_user_exists(patient_id):
                self.__records[patient_id] = {}
            self.__records[patient_id][timestamp] = {'abe': abe_cipher, 'aes': aes_cipher}
            return str(patient_id) + ";" + str(timestamp)
        print("[ERROR] Inserting failed for personal health record repository.")
        return ""

    def replace_file(self, user_id, file_name, abe_cipher, aes_cipher):
        """
        Replace a file and store the file in memory.
        Structure is: Dictionary with keys of userID containing
        dictionaries with keys of timestamps containing single records.
        {user_id: {timestamp: record}}
        :param user_id: The identifier of the patient.
        :param file_name: The identifier of the file.
        :param abe_cipher: The output of abe_encrypt containing the encrypted group element.
        :param aes_cipher: The output of aes_encrypt containing the encrypted record content.
        :return: Return the record_id of the inserted record.
        """
        file_name_split = file_name.split(";")
        patient_id = int(file_name_split[0])
        timestamp = int(file_name_split[1])
        if self.__check_user_id(user_id) and self.__check_user_id(patient_id) and self.__check_user_exists(patient_id):
            if not self.__ta.can_user_do_upload(user_id, patient_id):
                print("[ERROR] User with id " + str(user_id) + " can not replace for patient: " + str(patient_id))
                return ""
            self.__records[user_id][timestamp] = {'abe': abe_cipher, 'aes': aes_cipher}
            return str(user_id) + ";" + str(timestamp)
        print("[ERROR] Replacing failed for personal health record repository.")
        return ""

    def download_entire_user(self, user_id):
        """
        Returns all records for a specific patient.
        :param user_id: The user_id corresponding to a patient_id.
        :return: A dictionary with all records if they exist.
        """
        if self.__check_user_exists(user_id):
            return self.__records[user_id]
        else:
            return []

    def get_ids_from_user(self, user_id):
        """
        Returns a list of all record_ids for a specific patient.
        :param user_id: The user_id used for selection corresponding to a patient_id.
        :return: A list with all record_ids if they exist.
        """
        if self.__check_user_exists(user_id):
            return [f'{user_id};{k}' for k in self.__records[user_id].keys()]
        else:
            return []

    def download_single_record(self, record_id):
        """
        Returns a single health record based on a specific record_id.
        :param record_id: The record_id used for selection.
        :return: The selected record if it exists.
        """
        record_id = record_id.split(";")
        user_id = int(record_id[0])
        timestamp = int(record_id[1])
        if len(record_id) == 2:
            if self.__check_user_exists(user_id):
                if timestamp in self.__records[user_id].keys():
                    return self.__records[user_id][timestamp]
        return ""

    def __check_user_id(self, user_id):
        """
        Checks if the user_id is valid >=0
        :param user_id: The user id that has to be checked.
        :return: True/False if it is a valid user_id.
        """
        try:
            user_id = int(user_id)
            if user_id >= 0:
                return True
            else:
                print("[ERROR] Incorrect user_id for personal health record repository.")
        except ValueError:
            print("[ERROR] Incorrect user_id for personal health record repository.")
        return False

    def __check_user_exists(self, user_id):
        """
        Check if there exist any records for this patient.
        :param user_id: The user_id of the patient.
        :return: True/False if there are any records for this patient.
        """
        return user_id in self.__records.keys()
