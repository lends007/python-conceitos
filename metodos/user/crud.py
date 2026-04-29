from db import USERS
from encryption import encrypt_password
from validations import validate_email

def list_users():
    return [user for user in USERS]

def create_users(username, email, password):
    if not validate_email(email):
        return "email invalido"
    
    password_hash = encrypt_password(password)

    id = len(USERS) + 1
    new_user = {
        'id': id,
        'username': username,
        'email': email,
        'password': password_hash
    }


    USERS.append(new_user)
    return "email cadastrado com exito"

def update_users (id, username, email, password):
    if not validate_email(email):
        return "email invalido"
    
    password_hash = encrypt_password(password)

    USERS [id - 1] = {
        'id': id,
        'username': username,
        'email': email,
        'password': password_hash
    }
    return 'usuario atualizado com exito'

def remove_users (id):
    USERS.pop(id-1)
    return 'Usuario removido com exito'

