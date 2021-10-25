from User import UserClass
from TA import TAClass
from Role import ROLE


def main():
    print("Starting main program...")
    user_object_list = []
    user_role_amount = [2, 3, 2, 0, 0, 0]
    user_list = {0: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)
    # TODO init FS
    fs = 0

    # TODO initialize users based on the user_role_amount list
    for i in range(6):
        for amount in range(len(user_role_amount, user_role_amount+ user_role_amount[i], 1)):
            print(str(i) + " " + str(amount))
            #user_object_list.append(UserClass(0, ROLE(0), ta, fs))

    # TODO test that users have correct roles/ids
    

if __name__ == "__main__":
    main()
