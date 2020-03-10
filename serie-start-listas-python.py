#START LISTAS EM PYTHON

listaTeste = ['SP', 'MG', 'RJ', 'DF', 'SC', 'RS', 'RN', 'SE'] #criando lista

print(listaTeste) #imprimindo listas

listaTeste.append('AC') #adicionar texto ao final da lista

print(listaTeste)

listaTeste.append('RG') #adicionar texto ao final da lista

print(listaTeste)

listaTeste.insert(0,"RS") #inserir no indice desejado, indices são as posições onde as informações se encontram, começando em 0

print(listaTeste)

listaTeste.pop(1) #remover por índice, posição 

print(listaTeste)

listaTeste.insert(1,'SP')

print(listaTeste)

listaTeste.remove('RG') #remover por texto

#EXERCÍCIO: Faça um programa que peça 4 nomes e vá adicionando esses nomes dentro de uma lista. No final mostre a lista com esses 4 nomes. 


print('Exercício 1:')
listaNomes = []
for x in range (4):
    nome = input("digite o nome desejado: ")
    listaNomes.append(nome)
print(listaNomes)

#EXERCÍCIO: Faça um programa que mostre os itens de uma lista. Um em baixo do outro. 


print('Exercício 2:')
listaNomes = ['Ana', 'Maria', 'João', 'Matheus']
tamanhoLista = len(listaNomes) #função 'len' conta quantos números tem em uma lista

for x in range (tamanhoLista):  #loop se repete até o fim da lista
  print(listaNomes[x]) #x assume todos os valores até o fim da lista
  #ao final imprime cada valor um abaixo do outro









