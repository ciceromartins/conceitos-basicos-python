'''
1. Conceitos Básicos -> OK
2. Estruturas de Controle
3. Funções
4. Listas e Dicionários
5. Trabalhando com Arquivos
6. Tratamento de exceções (try, except)
7. Módulos e Bibliotecas
'''

# ESTRUTURAS DE CONTROLE
# ESTRUTURAS DE DECISAO -> Se acontece uma coisa, faz isso, se nao, faz aquilo
# ESTRUTURA DE REPETICAO -> Percorrer dados e exibi-los na tela (loop)
# ESTRUTURA MISCELENEA -> Possibilidade de parar ou continuar a execucao de um loop

# ESTRUTURAS DE DECISAO
# if, else, elif (else if)
idade = 18

# if (idade > 18):
#   print("Tem mais de 18 anos.")
# elif (idade == 18):
#   print("Tem exatamente 18 anos.")
# else:
#   print("É menor de idade!")
#   print("E não pode entrar.")
#   print("Mas eu que decido!")

# ESTRUTURAS DE REPETIÇÃO
# while e for
x = 1
# while x <= 5:
#   print(x)
#   x += 1

# print("-----")

# for x in range(10):
#   x += 1
#   print(x)

# ESTRUTURAS MISCELANEAS
x = 1
while x <= 5:
  print(x)
  x += 1
  if (x > 3):
    break

print("----")

for x in range(10):
  x += 1
  print(x)
  if (x > 5):
    continue
  print(x)
