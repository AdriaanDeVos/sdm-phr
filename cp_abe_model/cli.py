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
        for i in range(len(ROLE)):
            print(str(i+1) + ") " + ROLE(i).name)
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
            user_actions(users, users[choice-1])
            return
        elif choice == 0:
            return
        else:
            print("Input not recognized, please try again.")

def user_actions(users, user):
    while True:
        print("")
        print("=============================================")
        print("     You are currently logged in as: " + user.get_role().name)
        print("=============================================")
        print("")
        print("Please choose one of the following options:")
        print("0) Log-out")
        print("1) Create a new health record")
        print("2) Download and read a health record")
        if user.get_role().name == 'PATIENT':
            print("4) Provide read access to your health records")
        choice = input()
        if choice == "0":
            return
        elif choice == "1":
            create_new_record(users, user)
            print("Health record has been encrypted and uploaded!")
            print("")
        elif choice == "2":
            download_record(users, user)
            print("")
        else:
            print("Input not recognized, please try again.")

def create_new_record(users, user):
    print("")
    print("=============================================")
    print("  Creating a new entry in the health record")
    print("=============================================")

    while True:
        print("")
        print("Please choose the patient you want to upload for:")
        for i in range(len(users)):
            role = users[i].get_role().name
            if role == 'PATIENT':
                print(str(i+1) + ") " + users[i].get_role().name)
        choice = int(input("Choice: "))
        if 0 < choice <= len(users) and users[choice-1].get_role().name == 'PATIENT':
            print("Please enter the content of the health record:")
            message = input("Message:")
            print("Please enter the access policy for the health record:")
            print("Example = (PATIENT and RELATED-TO-0)")
            policy = input("Policy:")
            return user.encrypt_and_send(choice-1, message, policy)
        else:
            print("Input not recognized, please try again.")

def download_record(users, user):
    print("")
    print("=============================================")
    print("  Downloading and decrypting health records")
    print("=============================================")

    while True:
        print("")
        print("Please choose the user you want to view the records of:")
        for i in range(len(users)):
            print(str(i+1) + ") " + users[i].get_role().name)
        choice = int(input("Choice: "))
        if 0 < choice <= len(users):
            target_user = users[choice-1]
            files = target_user.file_server.get_ids_from_user(choice-1)
            while True:
                print("Please choose the record you want to download and decrypt:")
                for i in range(len(files)):
                    print(str(i+1) + ") " + files[i])
                choice = int(input("Choice: "))
                if 0 < choice <= len(files):
                    print(user.decrypt_from_send(files[choice-1]))
                    return
                else:
                    print("Input not recognized, please try again.")
        else:
            print("Input not recognized, please try again.")


if __name__ == "__main__":
    main()
