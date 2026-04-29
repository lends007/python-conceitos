user = [
    {"id": 1, "name": "joao", "active": True},
    {"id": 2, "name": "maria", "active": False},
    {"id": 3, "name": "pedro", "active": True},
    {"id": 4, "name": "gustavo", "active": False},
    {"id": 5, "name": "lucas", "active": True},
    {"id": 6, "name": "isaque", "active": False},
    {"id": 7, "name": "erick", "active": True},
    {"id": 8, "name": "matheus", "active": False},
    {"id": 9, "name": "vinicios", "active": True},
    {"id": 10, "name": "kelwin", "active": False},
    {"id": 11, "name": "maria", "active": True},
    {"id": 12, "name": "pedro", "active": False},
    {"id": 13, "name": "gustavo", "active": True},
    {"id": 14, "name": "lucas", "active": False},
    {"id": 15, "name": "isaque", "active": True},

]

active_users = [user for user in user if user["active"]]
inactive_users = [user for user in user if user["active"]]
print(f'Usuarios ativos: \n{active_users}\n')
print(f'Usuarios inativos: \n{inactive_users}\n')

nome = [user["name"] for user in user]
id = [user["id"] for user in user]
id_nao_ativos = [user ["id"] for user in user if not user ["active"]]
id_ativos = [user ["id"] for user in user if  user ["active"]]
print(f'Nomes de usuarios : \n{nome}\n')
print(f'IDS de Usuarios: \n{id}\n')
print(f'IDS de Usuarios Ativos: \n{id_ativos}\n')
print(f'IDS de Usuarios Inativos: \n{id_nao_ativos}\n')

price = [100.0, 250.0, 80.0, 150.0]
desconto_10 = [price * 0.9 for price in price if price]
desconto_20 = [price * 0.8 for price in price if price]
desconto_30 = [price * 0.7 for price in price if price]
desconto_40 = [price * 0.6 for price in price if price]
desconto_50 = [price * 0.5 for price in price if price]
print(f'Preços com desconto de 10%: \n{desconto_10}\n')
print(f'Preços com desconto de 20%: \n{desconto_20}\n')
print(f'Preços com desconto de 30%: \n{desconto_30}\n')
print(f'Preços com desconto de 40%: \n{desconto_40}\n')
print(f'Preços com desconto de 50%: \n{desconto_50}\n')

raw_email = [
    "joazinn@email.com",
    "KELWInn@email.coM                                         ",
    "joAOGORdo@EMAil.CoM",
    "GORdiNhO.coM"
]
print(f'Todos os Emails: \n{raw_email}\n')

striped_email = [email.strip() for email in raw_email]
print(f'Emails sem espaços em branco: \n{striped_email}\n') 

lower_emial = [email.lower() for email in striped_email]
print(f'Emails em letras minúsculas: \n{lower_emial}\n')

email = [email.strip().lower() for email in raw_email]
print(f'Emails sem espaços em branco e em letras minúsculas: \n{email}\n')

emails = [
    "jo      a   z  in   n@  em  ail   .co  m",
    "   K    EL    WIn    n@   ema      il  .c      o      M  ",
    "j  o   A  O  G  O  R  d  o  @  E  M  A  i  l  .  C  o  M  ",
    "G   O  R d i N h  O . c o M"
]
print(f'Emails bagunçados: \n{emails}')

emails_limpos = [  
    email.lower()
    .replace(" ", "")
    for email in emails
]
print(f'Emails limpos: \n {emails_limpos}\n')

# list comprehension e uma forma concisa 
# de criar listas a partir de iteraveis,
# aplicando uma expressão a cada item e
# opcionalmente filtrando os itens com uma condição.
# a sintaxe básica é: nova_lista = [expressão for item in iterável if condição]