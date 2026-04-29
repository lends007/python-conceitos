nome = 'cleber' #string
idade = 40 #int
altura = 1.85 #float
casado = True #boolean

if idade >= 18:
    #print(f'{nome} é maior de idade')
    print(f'{nome} é maior de idade')
elif idade >= 60:
    print(f'{nome} é idoso')

if altura >= 1.80:
    print(f'{nome} é alto')
elif altura >= 1.60:
    print(f'{nome} tem a aultura media')
elif altura >= 1.60 and altura < 1.60:
    print (f'{nome} é baixo')  

if casado:
    print(f'{nome} é casado')
elif not casado:
    print(f'{nome} é solteiro')

idade = 17
autorizacao = True
if idade >= 18 or autorizacao:
    print('pode entrar na festa')
else:
    print('não pode entrar na festa')