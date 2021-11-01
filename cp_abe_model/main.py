from User import UserClass
from TA import TAClass
from Role import ROLE
from phr_repo import PHRRepo


def main():
    print("Starting main program...")
    user_object_list = []
    user_role_amount = [2, 3, 2, 0, 4, 0]
    user_list = {}
    attr_list = ['PATIENT', 'HOSPITAL', 'HEALTH_CLUB', 'DOCTOR', "INSURANCE", "EMPLOYER"]
    for i in range(user_role_amount[0]):
        attr_list.append("RELATED-TO-"+str(i))
    for i in range(len(user_role_amount)):
        for j in range(user_role_amount[i]):
            user_list[len(user_list)] = [attr_list[i]]
            if i == 0:
                pat_id = len(user_list)-1
                new_attr = "RELATED-TO-"+str(pat_id)
                user_list[pat_id] = user_list[pat_id] + [new_attr]
    print(user_list)
    ta = TAClass(attr_list, user_list)
    fs = PHRRepo()

    for i in range(len(user_role_amount)):
        user_object_list = user_object_list + make_users(len(user_object_list), ROLE(i), ta, fs, user_role_amount[i])

    policy = '((RELATED-TO-0 and (PATIENT OR DOCTOR)))'
    message = "dekatkraptdekrullenvandetrap"
    print("Encrypting file...")
    file_id = user_object_list[0].encrypt_and_send(user_object_list[0].get_user_id(), message, policy)
    print("Decrypting file...")
    decr_message = user_object_list[0].decrypt_from_send(file_id)

    print("Successful decryption:", str(decr_message == message))


def make_users(user_id, role, ta, fs, amount):
    result = []
    for i in range(amount):
        result.append(UserClass(user_id + i, role, ta, fs))
    return result


if __name__ == "__main__":
    main()
