from crud import (create_users, update_users, list_users, remove_users)
from login import login 


opcao = ''

while True:
    opcao = input(
        'digite 1 das opções a seguir:\n'
        '1 - criar um novo usuário \n'
        '2 - atualizar um usuário \n'
        '3 - listar todos os usuários \n'
        '4 - remover um usuário \n'
        '0 - sair do programa \n'
        '5 - fazer login \n')	
    print('rodando...')
    match opcao:
       case '0':
            print('saindo do programa...')
            break
         
       case '1':
            username = input('digite o nome do usuário:')
            password = input('digite a senha do usuário:')
            email = input('digite o email do usuário:')
            create_users(username, password, email)

       case '2':
            print('atualizando um usuário...')

       case '3':
            print(list_users())

       case '4':
            user_id = int (input('digite o id do usuário:'))
            remove_users(user_id)

       case '5':
            username = input('digite o nome do usuário:')
            password = input('digite a senha do usuário:')
            print(login(username, password))