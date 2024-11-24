# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
nome = input('Qual seu nome')
total_dias = input('Quantos dias você vai estudar por semana')
total_horas = input('Quantas horas ira estudar por dia')
curso = input('Qual o seu curso')

total_dias = int(total_dias)
total_horas = int(total_horas )


print(f" O aluno {nome} estuda {curso}, {total_dias} dias por semana, {total_horas} horas por dia. Resultando em {total_horas*total_dias} horas semanais.")