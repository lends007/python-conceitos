from admin import Admin
from user import User

print('criação')
new_user = Admin.create_user(
    'jorge',
    'kelvin1234',
    'kelvinho133@gmail.com'

)
print(new_user)

new_admin = Admin.create_admin(
    'gustavo',
    'gustavinho1234',
    'gusta2432@gmail.com'
)


print('atualização')
Admin.update(new_user.id, 'pedrinho matador', 'pedrinho2327', 'pedrinhomtador@gmail.com')
Admin.update(new_admin.id, 'segio ramos', 'serginho2434', 'matador12@gmail.com')

print(Admin.get_user_by_id())
print('deleção')
Admin.delete(1)
print(Admin.get_all_users())


print("POHA DO GIT LIXO ")


