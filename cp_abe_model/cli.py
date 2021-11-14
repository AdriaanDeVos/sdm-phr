from TA import TA
from Role import ROLE


ta = TA() # The trusted authority used for setup and keygen.
users = [] # A list of all created users

"""
This file contains the CLI for interacting with the TA and file repository.
"""
def main():
    print("=============================================")
    print(" Welcome to the Personal Health System DASK™")

    while True:
        print("=============================================")
        print("You are currently logged in as: ADMINISTRATOR\n")
        print("Please choose one of the following options:")
        print("1) Create new user")
        print("2) Login as different user")
        choice = input("Choice: ")

        if choice == "1":
            users.append(create_new_user())
            print("Successfully created new user!\n")
        elif choice == "2":
            login_as_user()
            print("Logged out from user account.\n")
        else:
            print("Input not recognized, please try again.\n")

def create_new_user():
    """
    This function creates a new user account.
    :return: None
    """
    print("\n=============================================")
    print("            Creating a new user")
    print("=============================================")
    while True:
        print("\nPlease choose a role for the new user:")
        n_roles = len(ROLE)
        for i in range(n_roles):
            print(str(i + 1) + ") " + ROLE(i).name)
        choice = int(input("Choice: "))
        if 0 < choice < n_roles + 1:
            return ta.add_new_user(-1, ROLE(choice - 1))
        else:
            print("Input not recognized, please try again.")

def login_as_user():
    """
    This function logs in as a user.
    :return: None
    """
    print("\n=============================================")
    print("         Logging in as different user")
    print("=============================================")
    while True:
        print("\nPlease choose the user account:")
        print("0) Cancel logging in.")
        n_users = len(users)
        for i in range(n_users):
            print(str(i + 1) + ") " + users[i].get_role().name)
        choice = int(input("Choice: "))
        if 0 < choice <= n_users:
            user_actions(users[choice - 1])
            return
        elif choice == 0:
            return
        else:
            print("Input not recognized, please try again.")

def user_actions(user):
    """
    This function is used to interact as an user.
    :param user: The logged in user.
    :return: None
    """
    while True:
        print("\n=============================================")
        print("   You are currently logged in as: " + user.get_role().name + str(user.get_user_id()))
        print("=============================================\n")
        print("Please choose one of the following options:")
        print("0) Log-out")
        print("1) Create a new health record")
        print("2) View health record")
        if user.get_role().name == 'PATIENT':
            print("3) Provide read access to your health records")
            print("4) Provide write access to your health records")
        choice = input()
        if choice == "0":
            return
        elif choice == "1":
            create_new_record(user)
        elif choice == "2":
            download_record(user)
        elif choice == "3":
            grant_read_access(user)
        elif choice == "4":
            grant_write_access(user)
        else:
            print("Input not recognized, please try again.")

def create_new_record(user):
    """
    This function creates a new health record for the user.
    :param user: The user that is creating the health record.
    :return: None
    """
    print("\n=============================================")
    print("  Creating a new entry in the health record")
    print("=============================================")

    while True:
        print("\nPlease choose the patient you want to upload for:")
        possible_upload = False
        for i in range(len(users)):
            role = users[i].get_role().name
            if role == 'PATIENT' and ta.can_user_do_upload(user.get_user_id(), users[i].get_user_id()):
                print(str(i+1) + ") " + role + str(users[i].get_user_id()))
                possible_upload = True

        if not possible_upload:
            print("No patients available to upload for.")
            return

        choice = int(input("Choice: "))
        if 0 < choice <= len(users) and users[choice-1].get_role().name == 'PATIENT':
            print("Please enter the content of the health record:")
            message = input("Message:")
            print("Please enter the access policy for the health record:")
            print("Example = (PATIENT and RELATED-TO-0)")
            policy = input("Policy:")
            res = user.encrypt_and_send(choice-1, message, policy)
            if len(res) < 15:
                print("Health record has been encrypted and uploaded!")
            else:
                print("Health record was not created!")
            return
        else:
            print("Input not recognized, please try again.")

def download_record(user):
    """
    This function downloads and tries to decrypt a health record for the user.
    :param user: The user that is viewing the health record.
    :return: None
    """
    print("\n=============================================")
    print("  Downloading and decrypting health records")
    print("=============================================")

    while True:
        print("\nPlease choose the user you want to view the records of:")
        for i in range(len(users)):
            role = users[i].get_role().name
            if role == 'PATIENT':
                print(str(i+1) + ") " + role + str(users[i].get_user_id()))
        choice = int(input("Choice: "))
        if 0 < choice <= len(users):
            target_user = users[choice-1]
            files = target_user.file_server.get_ids_from_user(choice-1)
            while True:
                print("Please choose the record you want to download and decrypt:")
                if len(files) == 0:
                    print("No records available to download.")
                    return
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

def grant_read_access(user):
    """
    This function allows a patient to provide read access to his health records.
    :param user: The user that is giving out read permission.
    :return: None
    """
    print("\n=============================================")
    print("  Granting read access to your health records")
    print("=============================================")

    while True:
        print("\nPlease choose the user you want to give read access to:")
        possible = False
        for i in range(len(users)):
            role = users[i].get_role().name
            if role == 'DOCTOR' or role == 'INSURANCE' or role == 'EMPLOYER':
                print(str(i+1) + ") " + role + str(users[i].get_user_id()))
                possible = True

        if not possible:
            print("No eligible users available to give read access to.")
            return

        choice = int(input("Choice: "))
        chosen_users_role = users[choice-1].get_role().name
        if 0 < choice <= len(users) and (chosen_users_role == 'DOCTOR' or chosen_users_role == 'INSURANCE' or chosen_users_role == 'EMPLOYER'):
            res = ta.add_related_to_patient(user.get_user_id(), users[choice-1].get_user_id())
            if res:
                print("Read access has been granted!")
            else:
                print("Read access could not be granted!")
            return
        else:
            print("Input not recognized, please try again.")

def grant_write_access(user):
    """
    This function allows a patient to provide a hospital or health club with the ability to upload records.
    :param user: The user that is giving out write permission.
    :return: None
    """
    print("\n=============================================")
    print("  Granting write access to your health records")
    print("=============================================")

    while True:
        print("\nPlease choose the user you want to give write access to:")
        possible = False
        for i in range(len(users)):
            role = users[i].get_role().name
            if role == 'HOSPITAL' or role == 'HEALTHCLUB':
                print(str(i+1) + ") " + role + str(users[i].get_user_id()))
                possible = True

        if not possible:
            print("No eligible users available to give write access to.")
            return

        choice = int(input("Choice: "))
        chosen_users_role = users[choice-1].get_role().name
        if 0 < choice <= len(users) and (chosen_users_role == 'HOSPITAL' or chosen_users_role == 'HEALTHCLUB'):
            res = ta.add_related_to_patient(user.get_user_id(), users[choice-1].get_user_id())
            if res:
                print("Write access has been granted!")
            else:
                print("Write access could not be granted!")
            return
        else:
            print("Input not recognized, please try again.")

if __name__ == "__main__":
    main()
