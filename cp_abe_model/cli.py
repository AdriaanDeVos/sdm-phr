from TA import TA
from Role import ROLE

ta = TA()

def main():
    users = []
    print("=============================================")
    print(" Welcome to the Personal Health System DASK™")

    while True:
        print("=============================================")
        print("You are currently logged in as: ADMINISTRATOR")
        print("")
        print("Please choose one of the following options:")
        print("1) Create new user")
        print("2) Login as different user")
        choice = input("Choice: ")

        if choice == "1":
            users.append(create_new_user())
            print("Successfully created new user!")
            print("")
        elif choice == "2":
            login_as_user(users)
            print("Logged out from user account.")
            print("")
        else:
            print("Input not recognized, please try again.")

def create_new_user():
    print("")
    print("=============================================")
    print("            Creating a new user")
    print("=============================================")
    while True:
        print("")
        print("Please choose a role for the new user:")
        print("1) Patient")
        print("2) Hospital")
        print("3) Healthclub")
        print("4) Doctor")
        print("5) Insurance")
        print("6) Employer")
        choice = int(input("Choice: "))
        if 0 < choice < 7:
            return ta.add_new_user(-1, ROLE(choice - 1))
        else:
            print("Input not recognized, please try again.")

def login_as_user(users):
    print("")
    print("=============================================")
    print("         Logging in as different user")
    print("=============================================")
    while True:
        print("")
        print("Please choose the user account:")
        print("0) Cancel logging in.")
        for i in range(len(users)):
            print(str(i+1) + ") " + users[i].get_role().name)
        choice = int(input("Choice: "))
        if 0 < choice <= len(users):
            user_actions(users[choice-1])
            return
        elif choice == 0:
            return
        else:
            print("Input not recognized, please try again.")

def user_actions(user):
    print("")
    print("=============================================")
    print("You are currently logged in as: " + user.get_role().name)
    print("=============================================")
    while True:
        print("")
        print("Please choose one of the following options:")
        print("0) Log-out")
        print("1) Create a new health record")
        print("2) Download and read a health record")
        if user.get_role().name == 'PATIENT':
            print("4) Provide read access to your health records")
        choice = input()
        if True:
            return
        else:
            print("Input not recognized, please try again.")

if __name__ == "__main__":
    main()
