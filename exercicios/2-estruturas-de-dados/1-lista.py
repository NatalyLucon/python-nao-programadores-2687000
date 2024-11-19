# Crie uma lista apenas com elementos numéricos
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista = [1,2,3,4,5,'Nome','Idade','Altura',True]
print(lista)
# Imprima na tela apenas os 5 primeiros elementos da lista
print(list[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista[0:-1:2])
# Remova da lista o último item
lista.pop()
print(lista)
# Insira na lista um novo item
lista[7]='Peso'
print(lista)
# Remova da lista um item específico
lista.remove(5)
print(lista)