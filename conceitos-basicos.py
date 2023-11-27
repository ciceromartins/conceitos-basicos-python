'''
1. Conceitos Básicos
2. Estruturas de Controle
3. Funções
4. Listas e Dicionários
5. Trabalhando com Arquivos
6. Tratamento de exceções (try, except)
7. Módulos e Bibliotecas
'''

'''
CONCEITOS BÁSICOS
Variáveis e tipos de dados
Operadores de comparação
Operadores aritméticos e lógicos
'''

nome = "Cícero"
idade = 31
saldo = 10.50

sobrenome: str = "Martins"
filhos: int = 0

# str -> strings (textos)
# int -> numeros inteiros (1, 2, 3)
# float -> numeros com ponto flutuante (1.50, 4.4, 10)
# bool -> boleano (True ou False)

estaBloqueado: bool = False

# IMPRESSAO DOS RESULTADOS
# print(nome)
# print(idade)
# print(saldo)
# print(sobrenome)
# print(filhos)
# print(estaBloqueado)



# OPERADORES ARITMETICOS E LOGICOS
# OPERADORES ARITMETICOS
# + -> Soma
# - -> Subtração
# * -> Multiplicação
# / -> Divisão
# // -> Divisão Inteira
# % -> Módulo
# ** -> Potência

soma = 10 + 2 # 12
subtracao = 10 - 2 # 8
multiplicacao = 3 * 3 # 9
divisao = 10 / 2 # 5
divisaoInteira = 13 // 2 # 6
modulo = 9 % 4 # 1
potencia = 2 ** 3 # 8

# print(soma)
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(divisaoInteira)
# print(modulo)
# print(potencia)

# OPERADORES COMPARACAO
# > -> Maior que
# < -> Menor que
# >= -> Maior ou igual que
# <= -> Menor ou igual que
# == -> Igual
numeroA = 1
numeroB = 3
nomeA = "Cícero"
nomeB = "Rodrigo"
nomeC = "Cícero"

# print(numeroA > numeroB) # False
# print(numeroA < numeroB) # True
# print(numeroA >= numeroB) # False
# print(numeroA <= numeroB) # True
# print(numeroA == numeroB) # False
# print(nomeA > nomeB) # False
# print(nomeA == nomeB) # False
# print(nomeA == nomeC) # True

# OPERADORES LOGICOS
# AND -> E
# OR -> OU
# NOT -> NÃO (NEGAÇÃO)
x = True
y = False
print(x and y) # False -> AS DUAS CONDICOES PRECISAM SER SATISFEITAS
print(x or y) # True -> UMA DAS CONDICOES PRECISA SER SATISFEITA
print(not x) # False -> INVERTE O VALOR DO BOLEANO
print(not y) # True -> INVERTE O VALOR DO BOLEANO