# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
cursos = ('Python','Canvas','Ingles','Programação','Excel')
curso_python = 'Python'
curso_canvas = 'Canvas'
curso_ingles = 'Ingles'
curso_excel = 'Excel'
nota = {}
pergunta = input('Qual o seu curso: ')
if pergunta in curso_python:
  nota[curso_python] = int(input(f'Qual nota você da ao curso {curso_python}: '))
if pergunta in curso_canvas:
  nota[curso_canvas] = int(input(f'Qual nota você da ao curso {curso_canvas}: '))
if pergunta in curso_ingles:
  nota[curso_ingles] = int(input(f'Qual nota você da ao curso {curso_ingles}: '))
if pergunta in curso_excel:
  nota[curso_excel] = int(input(f'Qual nota você da ao curso {curso_excel}: '))
else:
  print(f'Não temos esse curso na lista.')

print(nota)

