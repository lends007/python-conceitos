"""

pessoas = [
  {
    "nome": "João",
     "idade": 30
},#pessoa0
  {
    "nome": "Maria",
     "idade": 25
},#pessoa1
  {
    "nome": "Pedro",
     "idade": 35
},#pessoa2
]
nomes = [] #cria uma lista vazia para armazenar os nomes das pessoas

nomes.append(pessoas[0]['nome'])
#adicina o valor do atributo "nome" da pessoa0 a lista de nomes
nomes.append(pessoas[1]['nome'])
#adicina o valor do a/]]tributo "nome" da pessoa1 a lista de nomes
nomes.append(pessoas[2]['nome'])
#adicina o valor do atributo "nome" da pessoa2 a lista de nomes

nome = [] #cria uma lista vazia para armazenar os nomes das pessoas
idades = [] #cria uma lista vazia para armazenar as idades das pessoas
for pessoa in pessoas:
    nomes.append(pessoa['nome']) #nova lista de nomes
    idades.append(pessoa['idade'])#nova listan de idades
    print(f'{nomes}, {idades}') 

    # quero o nome de cada pessoa e a idade de cada pessoa
    nome = pessoa["nome"] #acessa o valor do atributo "nome" da pessoa atual
    # quero a idade de cada pessoa em pessoas 
    idade = [pessoa["idade"] for pessoa in pessoas]
    print(nome)
    print(idade)


    """

    for i in ragr(30)