'''
1. Conceitos Básicos -> OK
2. Estruturas de Controle -> OK
3. Funções -> OK
4. Listas e Dicionários
5. Trabalhando com Arquivos
6. Tratamento de exceções (try, except)
7. Módulos e Bibliotecas
'''

# LISTAS E DICIONARIOS
# LISTAS
listaDeFrutas = ["banana", "maça", "pêra", "goiaba"]
#                    0        1       2        3

listaDeFrutas.append("tomate")
listaDeFrutas.insert(0, "abacaxi")
listaDeFrutas.remove("maça")

# for fruta in listaDeFrutas:
#   print(fruta)

# DICIONARIOS
dictPessoas = {
  "nome": "Cícero",
  "idade": 31,
  "cidade": "Alfenas"
}

dictPessoas["naturalidade"] = "Ipatinga"
del dictPessoas["cidade"]

print(dictPessoas)