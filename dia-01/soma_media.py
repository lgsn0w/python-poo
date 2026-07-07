# Tradução de: algoritmo SomaEMedia.alg (02-para)
# Estrutura: para → for / range
#
# Original em Portugol:
#
#   para i de 1 ate n faca
#     leia(nota)
#     soma <- soma + nota
#   fimpara

n = int(input("Quantas notas voce quer digitar? "))

soma = 0

for i in range(1, n + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma = soma + nota

media = soma / n

print("Soma das notas:", soma)
print("Media da turma:", round(media, 2))
