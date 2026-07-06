# Tradução de: algoritmo Tabuada.alg (02-para)
# Estrutura: para → for / range
#
# Original em Portugol:
#
#   para i de 1 ate 10 faca
#     resultado <- numero * i
#     escreval(numero, " x ", i, " = ", resultado)
#   fimpara

numero = int(input("Digite um numero inteiro: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
