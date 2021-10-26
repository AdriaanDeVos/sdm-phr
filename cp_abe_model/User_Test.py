from User import UserClass
from TA import TAClass
from Role import ROLE
from phr_repo import PHRRepo


def main():
    print("Starting user test...")
    user_object_list = []
    user_list = {0: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)
    fs = PHRRepo()

    user_object_list.append(UserClass(0, ROLE(0), ta, fs))

    user = user_object_list[0]

    policy = '((ONE and THREE) and (TWO OR FOUR))'
    message = "dekatkraptdekrullenvandetrap"
    file_id = user.encrypt_and_send(user.get_user_id(), message, policy)
    print(file_id)

    print("Successful decryption:", str(user.decrypt_from_send(file_id) == message))


if __name__ == "__main__":
    main()
