from db import USERS
from validation import validate_email
from encryption import encrypt_password
import asyncio

async def create_user(username, email, password):
    email_validated = await validate_email(email)
    if not email_validated:
        return 'email invalido'
    
    password_hash = await encrypt_password(password) 


    id = len(USERS) + 1
    new_user = {
        'id': id,
        'username': username,
        'email': email,
        'password': password_hash
    }

    USERS.append(new_user)
    return 'Usuário criado com sucesso'

async def list_users():
    return [user for user in USERS]

async def update_user(id, username, email, password):
    email_validated = await validate_email(email)
    if not email_validated:
        return 'email invalido'
    
    password_hash = await encrypt_password(password)
    
    USERS[id -1] = {    
        'id': id,
        'username': username,
        'email': email,
        'password': password_hash
    }
    return 'Usuário atualizado com sucesso'


async def remove_user(id):

    USERS.pop(id - 1)
    return 'Usuário removido com sucesso'