from TA import TA
from Role import ROLE


def main():
    print("Starting main program...")
    ta = TA()
    user_role_amount = [2, 3, 2, 0, 4, 0]
    users = make_users(ta, user_role_amount)

    policy = '((RELATED-TO-0 and (PATIENT OR DOCTOR)))'
    message = "dekatkraptdekrullenvandetrap"
    print("Encrypting file...")
    file_id = users[0].encrypt_and_send(users[0].get_user_id(), message, policy)
    print("Decrypting file...")
    decr_message = users[0].decrypt_from_send(file_id)

    print("Successful decryption:", str(decr_message == message))


def make_users(ta, user_role_amount):
    users = []
    for i in range(len(user_role_amount)):
        for j in range(user_role_amount[i]):
            users.append(ta.add_new_user(-1, ROLE(i)))
    return users


if __name__ == "__main__":
    main()
