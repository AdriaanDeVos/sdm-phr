from User import UserClass
from TA import TAClass
from Role import ROLE


def main():
    print("Starting main program...")
    user_object_list = []
    user_role_amount = [2, 3, 2, 0, 4, 0]
    user_list = {0: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)
    # TODO init FS
    fs = 0

    for i in range(len(user_role_amount)):
        user_object_list = user_object_list + make_users(len(user_object_list), ROLE(i), ta, fs, user_role_amount[i])

    for user in user_object_list:
        print(str(user.get_user_id()) + " " + str(user.get_role()))


def make_users(user_id, role, ta, fs, amount):
    result = []
    for i in range(amount):
        result.append(UserClass(user_id + i, role, ta, fs))
    return result


if __name__ == "__main__":
    main()
