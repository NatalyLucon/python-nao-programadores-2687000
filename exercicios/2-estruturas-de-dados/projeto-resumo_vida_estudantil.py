# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula 
# em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados 
# e (apenas) o primeiro e último curso.
dados = {}
dados['nome'] = input('Qual o seu nome: ')
dados['ano'] = input('Qual ano você conheceu o Linkedin: ')
dados['ano_atual']=input('Em qual ano estamos: ')
cursos_input = input('Quais os cursos você já fez? (separe-os com vírgula): ')

dados['curso'] = [curso.strip() for curso in cursos_input.split(',')]

dados['ano'] = int(dados['ano'])
dados['ano_atual']=int(dados['ano_atual'])


print(f"O nome do estudante é {dados['nome']}, conheceu o Linkedin em {dados['ano']}, passados {dados['ano_atual']-dados['ano']}. Já realizou os cursos {dados['curso']}, com o primeiro curso sendo {dados['curso'][0]} e último {dados['curso'][-1]}. ")