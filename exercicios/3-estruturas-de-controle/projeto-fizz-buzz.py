# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
lista = list(range(0,15))
print(lista)
valor = 0 
for item in lista:
  if item % 3 == 0 and item % 5 == 0:
    lista[valor] = 'FizzBuzz'
  elif item % 3 == 0:
    lista[valor] = 'Fizz'
  elif item % 5 == 0:
    lista[valor] = 'Buzz'
  else: 
    lista[valor] = item
  valor +=1
print(lista)