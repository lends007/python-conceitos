
uteis = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira")
fim_de_semana = ("Sábado", "Domingo")

hoje = "Segunda-feira" 

if hoje in uteis:
    print("Hoje é um dia útil.")
elif hoje in fim_de_semana:
    print("Hoje é um dia de descanso.")


idade = int(input("Digite sua idade: "))
tem_carteira = input("Você possui carteira de habilitação? (Sim/Não): ").lower()

if idade >= 18 and tem_carteira == "sim":
    print("Autorizado: Você tem idade e habilitação para dirigir.")

elif idade >= 18 and tem_carteira == "não":
    print("Negado: Você tem idade, mas precisa tirar a habilitação primeiro.")

elif idade < 18:
    print("Negado: Você é menor de idade e não pode dirigir, com ou sem carteira.")

else:
    print("Opção inválida. Por favor, responda com Sim ou Não.")


altura = float(input("Digite sua altura em metros (ex: 1.75): "))

if altura < 1.45:
    print("Classificação: Nanismo")

elif 1.45 <= altura < 1.65:
    print("Classificação: Baixo")

elif 1.65 <= altura < 1.85:
    print("Classificação: Médio")

elif 1.85 <= altura < 2.10:
    print("Classificação: Alto")

else:
    print("Classificação: Gigantismo")
  