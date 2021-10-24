from charm.toolbox.pairinggroup import PairingGroup, GT
from ABE.bsw07 import BSW07
from TA import TAClass


def main():
    user_list = {0: ['ONE', 'TWO', 'THREE', 'FOUR']}
    attr_list = ['ONE', 'TWO', 'THREE']
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

    # TODO "Upload" file from TA

    # TODO "Download" file from TA

    # Decrypt
    rec_msg = cpabe.decrypt(pk, ctxt, key)
    if rec_msg == msg:
        print("Successful decryption.")
    else:
        print("Decryption failed.")


if __name__ == "__main__":
    debug = False
    main()