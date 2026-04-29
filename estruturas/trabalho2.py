"""
usuario_salvo = "admin"
senha_salva = "1234"

usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")

if usuario_digitado == usuario_salvo and senha_digitada == senha_salva:
    print("LOGIN BEM SUCEDIDO")

elif usuario_digitado == usuario_salvo and senha_digitada != senha_salva:
    print("SENHA INCORRETA")

elif senha_digitada == senha_salva and usuario_digitado != usuario_salvo:
    print("USUÁRIO INCORRETO")

else:
    print("USUÁRIO E SENHA INCORRETOS")
"""

anos_empresa = 11
escolaridade = "mestrado" 
bom_historico = True

if anos_empresa > 10 and escolaridade == "mestrado" and bom_historico:
    print("Promovido a: GERENTE GERAL")

elif anos_empresa > 8 and escolaridade == "pós-graduação" and bom_historico:
    print("Promovido a: GERENTE DO SETOR")

elif anos_empresa > 5 and escolaridade == "graduação" and bom_historico:
    print("Promovido a: SUPERVISOR")

else:
    print("Ainda não atende aos requisitos para as promoções de cargo.")
