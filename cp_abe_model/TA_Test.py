import hashlib

from charm.toolbox.pairinggroup import PairingGroup, GT
from TA import TAClass
from ABE.bsw07 import BSW07
from Crypto.Cipher import AES


def main():
    # SETUP TA
    user_list = {0: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)

    # SETUP USER
    pairing_group = PairingGroup('MNT224')
    cpabe = BSW07(pairing_group, 2)
    public_key = ta.get_pk()
    user_key = ta.key_request(0)

    # Encrypt Message (https://en.wikipedia.org/wiki/Hybrid_cryptosystem)
    policy_str = '((ONE and THREE) and (TWO OR FOUR))'
    random_group_element = pairing_group.random(GT)
    message = "testtesttesttest"

    encrypt_aes_key = hashlib.sha256(str(random_group_element).encode('utf-8')).digest()
    encrypted_group_element = cpabe.encrypt(public_key, random_group_element, policy_str)

    cipher = AES.new(encrypt_aes_key)
    ciphertext = cipher.encrypt(message)

    # Upload Message
    # TODO: Make sure both the encrypted text, and the encrypted key is uploaded and returned.
    file_name = "0_random_25/10/2021"
    ta.upload_file(file_name, ciphertext)
    obtained_file_names = ta.get_file_ids()
    print("file_name in ta.get_file_ids()?:", file_name in obtained_file_names)

    obtained_ct = ta.get_file(file_name)

    # Decrypt Message
    decrypted_group_element = cpabe.decrypt(public_key, encrypted_group_element, user_key)
    decrypt_aes_key = hashlib.sha256(str(decrypted_group_element).encode('utf-8')).digest()
    plaintext = AES.new(decrypt_aes_key).decrypt(ciphertext).decode("utf-8")

    if plaintext == message:
        print("Successful decryption.")
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    main()