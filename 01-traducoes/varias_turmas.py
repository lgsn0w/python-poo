# Tradução de: pdf-ex1-varias-turmas.alg (03-enquanto)
# Estruturas: enquanto (controla turmas) + para (le notas) + se
#
# Original em Portugol:
#
#   enquanto (resposta = "S") faca
#     para i de 1 ate n faca
#       leia(nota)
#       se (nota >= 7) entao
#         aprovados <- aprovados + 1
#       fimse
#     fimpara
#   fimenquanto

resposta = input("Deseja cadastrar uma turma? (S/N): ").upper()

while resposta == "S":
    n = int(input("Quantos alunos tem a turma? "))
    soma = 0
    aprovados = 0

    for i in range(1, n + 1):
        nota = float(input(f"Nota do aluno {i}: "))
        soma = soma + nota
        if nota >= 7:
            aprovados = aprovados + 1

    media = soma / n
    print(f"Media da turma: {media:.2f}")
    print(f"Aprovados: {aprovados}")

    resposta = input("Deseja cadastrar outra turma? (S/N): ").upper()

print("Programa encerrado.")
