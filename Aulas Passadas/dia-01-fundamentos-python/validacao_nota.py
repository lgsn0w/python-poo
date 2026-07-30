# Tradução de: pptx-ex1-validacao-nota.alg (03-enquanto)
# Estruturas: enquanto → while / se senao → if else
#
# Original em Portugol:
#
#   enquanto (nota < 0) ou (nota > 10) faca
#     escreval("Nota invalida!")
#     leia(nota)
#   fimenquanto
#
#   se (nota >= 7) entao
#     escreval("Aprovado")
#   senao
#     escreval("Reprovado")
#   fimse

nota = float(input("Digite uma nota (0 a 10): "))

while nota < 0 or nota > 10:
    print("Nota invalida!")
    nota = float(input("Digite novamente: "))

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
