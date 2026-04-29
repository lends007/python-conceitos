"""
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
saudacao("Maria")  
saudacao("Pedro")
saudacao("Ana") 
saudacao("Carlos")"""
cadastro = [
{
    "usaname": "João",
    "password": "123456"
},
{
    "usaname": "Maria",
    "password": "abcdef"
},
{
    "usaname": "Pedro",
    "password": "qwerty"
},
{
    "usaname": "Ana",
    "password": "zxcvbn"
},
{
    "usaname": "Carlos",
    "password": "asdfgh"
}
]
def formacao_usuario(username):
    return username.replace(' ', "").lower()

def cadastro_usuario(valid_username, password):
    valid_username = formacao_usuario(valid_username)
    print(valid_username)
    for cadastros in cadastro:
        if cadastro ["username"] == valid_username:
            return 'Usuário já existe.'
    cadastros.append({
        "username": valid_username,
        "password": password
    })
    return "usuario cadastrado com sucesso"

print(cadastro("Jo a n z inn  ", "42343"))
print(cadastro('Maria', 'abcdef'))
print(cadastro('Pedro', 'qwerty'))
print(cadastro('Ana', 'zxcvbn'))

print(cadastro)('P a o  l a', '123456')

def atualizar_senha(username, new_password):
    valid_username = formatacao_usuario(username)
    for user in list:
         if user['username'] == valid_username:
            user['password'] = new_password
            return 'Senha atualizada com sucesso.'
    return 'Usuário não encontrado.'

print(atualizar_senha(cadastro, 'Jo a n z inn  ', 'nova_senha'))   
print(atualizar_senha(cadastro, 'Maria', 'nova_senha'))     

