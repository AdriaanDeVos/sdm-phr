import time

# Personal Health Record Repository Class
class PHRRepo:
    __records = {}

    def upload_file(self, user_id, file_content):
        if self.__check_user_id(user_id):
            timestamp = int(time.time())
            if not self.__check_user_exists(user_id):
                self.__records[user_id] = {}
            self.__records[user_id][timestamp] = file_content
            return str(user_id) + ";" + str(timestamp)
        print("[ERROR] Inserting failed for personal health record repository.")
        return ""

    def upload_ciphers(self, user_id, abe_cipher, aes_cipher):
        return self.upload_file(user_id, abe_cipher + ';' + aes_cipher)

    def download_entire_user(self, user_id):
        if self.__check_user_exists(user_id):
            return self.__records[user_id]
        else:
            return {}

    def download_single_record(self, record_id):
        record_id = record_id.split(";")
        user_id = int(record_id[0])
        timestamp = int(record_id[1])
        if len(record_id) == 2:
            if self.__check_user_exists(user_id):
                if timestamp in self.__records[user_id].keys():
                    return self.__records[user_id][timestamp]
        return ""

    def __check_user_id(self, user_id):
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
        return user_id in self.__records.keys()

    def test(self):
        print(self.__records)