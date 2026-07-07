# Tradução de: pptx-ex2-soma-sentinela.alg (03-enquanto)
# Estrutura: enquanto com sentinela → while com sentinela
#
# Original em Portugol:
#
#   enquanto (num <> 0) faca
#     soma <- soma + num
#     cont <- cont + 1
#     leia(num)
#   fimenquanto

soma = 0
cont = 0

num = float(input("Numero (0 para sair): "))

while num != 0:
    soma = soma + num
    cont = cont + 1
    num = float(input("Numero (0 para sair): "))

print("Soma:", soma)
print("Quantidade de numeros:", cont)
