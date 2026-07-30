# Tradução de: pdf-ex2-sistema-pedidos.alg (03-enquanto)
# Estruturas: enquanto (menu) + para (itens do pedido)
#
# Original em Portugol:
#
#   enquanto (opcao <> 2) faca
#     se (opcao = 1) entao
#       para i de 1 ate quantidade faca
#         leia(preco)
#         total <- total + preco
#       fimpara
#     fimse
#   fimenquanto

opcao = 0

while opcao != 2:
    print("1 - Fazer pedido")
    print("2 - Sair")
    opcao = int(input("Escolha: "))

    if opcao == 1:
        quantidade = int(input("Quantos itens no pedido? "))
        total = 0

        for i in range(1, quantidade + 1):
            preco = float(input(f"Preco do item {i}: "))
            total = total + preco

        print(f"Total do pedido: R$ {total:.2f}")

print("Sistema encerrado.")
