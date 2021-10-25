from charm.toolbox.pairinggroup import PairingGroup, GT
from TA import TAClass


def main():
    user_list = {0: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)
    cpabe = ta.get_cp_abe()

    # instantiate a bilinear pairing map
    # TODO Mag de user deze hebben?
    pairing_group = PairingGroup('MNT224')
    # TODO Change message
    msg = pairing_group.random(GT)

    pk = ta.get_pk()
    key = ta.key_request(0)

    # Encrypt
    policy_str = '((ONE and THREE) and (TWO OR FOUR))'
    ctxt = cpabe.encrypt(pk, msg, policy_str)

    file_name = "0_random_25/10/2021"
    ta.upload_file(file_name, ctxt)
    obtained_file_names = ta.get_file_ids()
    print("file_name in ta.get_file_ids()?:", file_name in obtained_file_names)

    obtained_ct = ta.get_file(file_name)

    # Decrypt
    rec_msg = cpabe.decrypt(pk, obtained_ct, key)
    if rec_msg == msg:
        print("Successful decryption.")
    else:
        print("Decryption failed.")


if __name__ == "__main__":
    debug = False
    main()