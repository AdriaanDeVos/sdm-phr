from User import UserClass
from TA import TAClass
from Role import ROLE


def main():
    print("Starting user test...")
    print(ROLE(0))
    user_object_list = []
    user_list = {0: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)
    # TODO init FS
    fs = 0

    user_object_list.append(UserClass(0, ROLE(0), ta, fs))

    user = user_object_list[0]
    print(user.get_user_id())
    print(user.get_role())
    # TODO
    """
    encrypt_and_send(self, message, policy)
    decrypt_and_send(self, message_id)
    """


if __name__ == "__main__":
    main()
