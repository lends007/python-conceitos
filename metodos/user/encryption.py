def encrypt_password(password): #maria123
    encrypt_password = ""
    for character in password:

          new_character = chr(ord(character) + 3)
          encrypt_password += new_character

    return encrypt_password

def decrypt_password(password):
     decrypt_password = ""

     for character in password:
            new_character = chr(ord(character) - 3)
            decrypt_password += new_character

     return decrypt_password

print('maria123')
print(encrypt_password('maria123'))
print(decrypt_password(encrypt_password('maria123')))