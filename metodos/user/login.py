from db import USERS
from encryption import decrypt_password

async def find_by_username(username):
    for user in USERS:
        if user['username'] == username:
            return user
        return None
    

async def login(username, password):
    user = await find_by_username(username)
    if user is None:
        return "Login falhou: usuário não encontrado"
    decrypted_password = await decrypt_password(user['password'])
    if decrypted_password == password:
        return "Login bem-sucedido"
    return "Login falhou: senha incorreta"
