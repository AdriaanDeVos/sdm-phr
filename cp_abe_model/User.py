
class User:
    def __init__(self, user_id, role, ta, fs):
        self.__user_id = user_id
        self.__role = role
        self.__ta = ta
        self.__user_key = ta.key_request(user_id)
        self.__file_server = fs
