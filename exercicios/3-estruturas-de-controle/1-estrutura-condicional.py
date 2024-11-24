# Declare 4 variáveis do tipo numérica
x = 3
y = 6
z = 20
w = 31
# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if x > w:
  print(f'Condição verdadeira onde {x} > {w}') 
elif y < z or z < w: 
  print(f'Condição 2 verdadeira onde {y} < {z} ou {z} < {w}') 
else:
  print(f'Nenhuma condição é verdadeira. {x} não é > {w} {y} não é < {z} ou {z} não é < {w}')

if x > w:
  print(f'Condição verdadeira onde {x} > {w}') 
elif y > z or z > w: 
  print(f'Condição 2 verdadeira onde {y} > {z} ou {z} > {w}')
elif (x*w) < (y*z) and (z/x) > (w/y):
  print(f'Condição 3 é verdadeira onde {(x*w)} > {(y*z)} e {(z/x)} > {(w/y)}.')
else:
  print(f'Nenhuma condição é verdadeira. {x} não é > {w}, {y} não é > {z} ou {z} não é > {w} e {(x*w)} não é > {(y*z)} e {(z/x)} não é > {(w/y)}.')
