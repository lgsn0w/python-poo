# Tradução de: pptx-ex3-menu.alg (03-enquanto)
# Estruturas: enquanto + se/senao encadeado → while + if/elif/else
#
# Original em Portugol:
#
#   enquanto (opcao <> 3) faca
#     se (opcao = 1) entao
#       ...
#     senao
#       se (opcao = 2) entao
#         ...
#       senao
#         escreval("Opcao invalida.")
#       fimse
#     fimse
#   fimenquanto
#
# Em Python usamos elif para evitar o aninhamento de senao se

print("1 - Somar  2 - Subtrair  3 - Sair: ", end="")
opcao = int(input())

while opcao != 3:
    if opcao == 1:
        a = float(input("Primeiro numero: "))
        b = float(input("Segundo numero: "))
        print("Resultado:", a + b)
    elif opcao == 2:
        a = float(input("Primeiro numero: "))
        b = float(input("Segundo numero: "))
        print("Resultado:", a - b)
    else:
        print("Opcao invalida.")

    print("1 - Somar  2 - Subtrair  3 - Sair: ", end="")
    opcao = int(input())

print("Programa encerrado.")
