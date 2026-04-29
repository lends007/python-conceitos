nome = ['Joao', 'Maria', 'Pedro', 'Gustavo']
#      index0    index1    index2    index3
#      index-4   index-3   index-2   index-1
"""
print(nome[0]) #acessando o primeiro index da lista
print(nome[1]) #acessando o segundo index da lista
print(nome[2]) #acessando o terceiro index da lista
print(nome[3]) #acessando o quarto index da lista

#acessando pelo tamanho da lista
print(nome[len(nome)-1]) #acessa o ultimo elemento da lista
print(nome[-1]) #acessa o ultimo elemento da lista
print(nome[-2]) #acessa o penultimo elemento da lista
print(nome[-3]) #acessa o antepenultimo elemento da lista
print(nome[-4]) #acessa o antepenultimo elemento da lista
"""

#modificando um elemento da lista
nome[0] = 'kelwin'
nome[1] = 'gustavo'
nome[2] = 'maria'
nome[3] = 'joao'
print(nome)

#adicione elemento na lista
nome.append('lucas')
nome.append('isaque')
nome.append('erick')
nome.append('matheus')
nome.append('vinicios')
nome.insert(0, 'isaque')
print(nome)

nome.remove('lucas')
print(nome)


