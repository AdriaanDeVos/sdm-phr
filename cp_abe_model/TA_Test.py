import hashlib
import base64

from charm.toolbox.pairinggroup import PairingGroup, GT
from TA import TAClass
from phr_repo import PHRRepo
from ABE.bsw07 import BSW07
from Crypto.Cipher import AES


def main():
    user_id = 0
    # SETUP PHRRepo
    repo = PHRRepo()

    # SETUP TA
    user_list = {user_id: ['ONE', 'TWO', 'THREE']}
    attr_list = ['ONE', 'TWO', 'THREE', 'FOUR']
    ta = TAClass(attr_list, user_list)

    # SETUP USER
    pairing_group = PairingGroup('MNT224')
    cpabe = BSW07(pairing_group, 2)
    public_key = ta.get_pk()
    user_key = ta.key_request(user_id)

    # Encrypt Message (https://en.wikipedia.org/wiki/Hybrid_cryptosystem)
    policy_str = '((ONE and THREE) and (TWO OR FOUR))'
    random_group_element = pairing_group.random(GT)
    message = "testtesttesttest"

    encrypt_aes_key = hashlib.sha256(str(random_group_element).encode('utf-8')).digest()
    encrypted_group_element = cpabe.encrypt(public_key, random_group_element, policy_str)

    cipher = AES.new(encrypt_aes_key)
    ciphertext = cipher.encrypt(message)

    # TODO ensure a correct textual format for sending this information as the original objects shouldn't be used...
    encrypted_message = str(encrypted_group_element) + ";" + str(base64.b64encode(ciphertext))

    # Upload Message
    upload_id = repo.upload_file(user_id, encrypted_message)
    repo.test()
    print(upload_id)

    # Download Message
    health_record = repo.download_single_record(upload_id).split(";")
    abe_cipher = health_record[0]
    aes_cipher = base64.b64decode(health_record[1])

    # Decrypt Message
    # TODO update with retrieved ciphers instead of "saved" ciphers.
    decrypted_group_element = cpabe.decrypt(public_key, encrypted_group_element, user_key)
    decrypt_aes_key = hashlib.sha256(str(decrypted_group_element).encode('utf-8')).digest()
    plaintext = AES.new(decrypt_aes_key).decrypt(ciphertext).decode("utf-8")

    if plaintext == message:
        print("Successful decryption.")
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    main()