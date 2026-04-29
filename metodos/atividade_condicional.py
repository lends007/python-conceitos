"""""
Tempo_limpo = True
Tempo_sujo = False
dia_da_semana = True

if dia_da_semana and Tempo_limpo:
    print('ir de bike para a escola')
elif dia_da_semana and Tempo_sujo:
    print('ir de carro para a escola')
else:
    print('Não é necessário ir para a escola')

email__valido = True

if email__valido:
    print('Enviar email')

    def enviar_email(email):
        if email:
          return 'Email enviado com sucesso!'
        return 'Email inválido. Por favor, tente novamente.'
    
    print(enviar_email(email__valido))
"""

""""
ATIVIDADES:
1 - FAZER UMA ESTRUTURA DE IF/ELIF/ELSE QUE
VERIFIQUE SE O DIA É DIA DE SEMANA OU NÃO

Dia = ' Domingo'

Dias_da_semana = ['Segunda','Terça','Quarta','Quinta','Sexta']
Final_de_semana = ['Sabádo','Domingo']

if Dia in Dias_da_semana:
  print('É dia de semana')
else:
  print('É final de semana')



2 - FAZER UMA ESTRUTURA DE IF/ELIF/ELSE QUE
VERIFIQUE SE UMA PESSOA PODE DIRIGIR OU NÃO,
LEVANDO EM CONSIDERAÇÃO AS VARIÁVEIS
TEM_CARTEIRA E IDADE

Tem_carteira = False
Idade = 18

if  Idade  >= 18 and Tem_carteira:
   print('Pode dirigir')
elif Idade >= 18 and Tem_carteira:
  print('Não pode dirigir')
else:
  print('Não pode dirigir pq é menor de idade')



3 - FAZER UMA ESTRUTURA DE IF/ELSE/ELIF QUE
VERIFIQUE A ALTURA DE UMA PESSOA, DIZENDO SE
ELE TEM NANISMO, SE É BAIXO, MÉDIO, ALTO, OU TEM
GIGANTISMO

Altura = 1.85

if Altura >= 1.90 and  Altura <= 2.05:
   print('Você é Gigante')
elif Altura >= 1.85 and Altura <= 1.90:
    print('Você é Alto')
elif Altura >= 1.65 and Altura <= 1.75 :
    print('Você tem uma altura media')
elif Altura >= 1.50 and Altura <= 1.60:
    print('Você tem uma altura Baixa')
else:
    print('Você tem Nanismo')

4 - CRIE UMA ESTRUTURA CONDICIONAL QUE SIMULE O LOGIN:
SE  O USUARIO E SENHA ESTIVEREM CORRETOS: LOGIN BEM SUCEDIDO
SENÃO, SE USUÁRIO ESTIVER CORRETO E SENHA INCORRETA: SENHA INCORRETA
SENÃO, SE SENHA ESTIVER CORRETA E USUÁRIO ESTIVER INCORRETO, USUÁRIO INCORRETO




Usuario = 'jackson'
senha = 'jackson123'

Usuario_correto = 'jackson'
senha_correta = 'jackson123'

if Usuario == Usuario_correto and senha == senha_correta:
    print('Login bem sucedido')
elif Usuario != Usuario_correto:
    print('Usuario incorreta')
elif senha != senha_correta:
    print('senha incorreto')


Usuario = {
   'username': 'jackson',
   'senha': 'jackson123'

}

Usuario_correto = 'jackson'
senha_correta = 'jackson123'

if Usuario['username'] == Usuario_correto and Usuario['senha'] == senha_correta:
    print('Login bem sucedido')
elif Usuario['username'] != Usuario_correto:
    print('Usuário incorreta')
elif Usuario['senha'] != senha_correta:
    print('senha incorreto')


5 - CRIE UMAESTRUTURA CONDICIONAL QUE SIMULE AS PROMOÇÕES DE UMA EMPRESA:
SE  O FUNCIONÁRIO  TEM MAIS DE 5 ANOS DE EMPRESA, TEM GRADUAÇÃO E TEM UM BOM HISTÓRICO: PODE SER SUPERVISOR
SENÃO, SE O FUNCIONÁRIO TEM MAIS DE 8 ANOS DE EMPRESA, TEM PÓS GRADUAÇÃO, E TEM UM BOM HISTÓRICO: PODE SER GERENTE DO SETOR
SENÃO, SE O FUNCIONÁRIO TIVER MESTRADO, TIVER MAIS DE 10 ANOS DE EMPRESA, E UM BOM HISTÓRICO, PODE SER GERENTE GERAL
funcionario = {
    'tempo_empresa': 15,
    'formacao': 'Mestrado',
    'bom_historico': True
  }
formacao_supervisor = ['Graduação', 'pós Graduação', 'Mestrado', 'Doutorado']
formacao_Gerente_setor = ['pós Graduação', 'Mestrado', 'Doutorado']
formacao_Gerente_geral = ['Mestrado', 'Doutorado']

if funcionario['tempo_empresa'] >= 10 and funcionario['formacao']  in  formacao_Gerente_geral and funcionario['bom_historico']:
    print('Pode ser Gerente geral')
elif funcionario['tempo_empresa'] >= 8 and funcionario['formacao']  in formacao_Gerente_setor and funcionario['bom_historico']:
    print('Pode ser Gerente do setor')
elif funcionario['tempo_empresa'] >= 5 and funcionario['formacao']  in formacao_supervisor and funcionario['bom_historico']:
    print('Pode ser supervisor')
elif not funcionario['bom_historico']:
    print('Não pode ser promovido por ter um histórico ruim')

Dia = 'Segunda'

match Dia:
    case 'Segunda': print('Dia de semana')
    case 'Terça': print('Dia de semana')
    case 'Quarta': print('Dia de semana')
    case 'Quinta': print('Dia de semana')
    case 'Sexta': print('Dia de semana')
    case 'Sabádo': print('Final de semana')
    case 'Domingo': print('Final de semana')

def login(username, password):
    correct_username = 'jackson'
    correct_username = 'jackson123'
    if username == correct_username and password == correct_password:
        return 'Login bem sucedido'
    return 'Login falhou. Verifique seu nome de usuário e senha e tente novamente."""