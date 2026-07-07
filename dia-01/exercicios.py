# ─────────────────────────────────────────────
#  EXERCÍCIOS — TRADUÇÃO PORTUGOL → PYTHON
#  Traduza cada algoritmo abaixo para Python.
#  Não apague os comentários de enunciado.
# ─────────────────────────────────────────────


# ═══════════════════════════════════════════
# EXERCÍCIO 1 — se / senao
# ═══════════════════════════════════════════
# Traduza o algoritmo abaixo para Python:
#
#   algoritmo "ClassificaIdade"
#   var
#      idade: inteiro
#   inicio
#      escreva("Digite sua idade: ")
#      leia(idade)
#      se idade < 12 entao
#         escreval("Crianca")
#      senao
#         se idade < 18 entao
#            escreval("Adolescente")
#         senao
#            escreval("Adulto")
#         fimse
#      fimse
#   fimalgoritmo
#
# DICA: em Python, use elif para evitar o senao se aninhado.

# SEU CÓDIGO AQUI:


# ═══════════════════════════════════════════
# EXERCÍCIO 2 — para
# ═══════════════════════════════════════════
# Traduza o algoritmo abaixo para Python:
#
#   algoritmo "ContadorPar"
#   var
#      i, n: inteiro
#   inicio
#      escreva("Ate qual numero? ")
#      leia(n)
#      para i de 1 ate n faca
#         se (i mod 2 = 0) entao
#            escreval(i)
#         fimse
#      fimpara
#   fimalgoritmo
#
# DICA: em Python, o operador "mod" (resto da divisão) é o "%".
#       i mod 2 = 0  →  i % 2 == 0

# SEU CÓDIGO AQUI:


# ═══════════════════════════════════════════
# EXERCÍCIO 3 — enquanto
# ═══════════════════════════════════════════
# Traduza o algoritmo abaixo para Python:
#
#   algoritmo "ContagemRegressiva"
#   var
#      n: inteiro
#   inicio
#      escreva("Digite um numero positivo: ")
#      leia(n)
#      enquanto (n <= 0) faca
#         escreval("Numero invalido!")
#         escreva("Digite novamente: ")
#         leia(n)
#      fimenquanto
#      enquanto (n >= 0) faca
#         escreval(n)
#         n <- n - 1
#      fimenquanto
#      escreval("Fim!")
#   fimalgoritmo

# SEU CÓDIGO AQUI:


# ═══════════════════════════════════════════
# EXERCÍCIO 4 — enquanto + para + se (desafio)
# ═══════════════════════════════════════════
# Traduza o algoritmo abaixo para Python:
#
#   algoritmo "AlunosPorTurma"
#   var
#      resposta: caractere
#      n, i, aprovados: inteiro
#      nota, soma, media: real
#   inicio
#      escreva("Cadastrar turma? (S/N): ")
#      leia(resposta)
#      enquanto (resposta = "S") faca
#         escreva("Quantos alunos? ")
#         leia(n)
#         soma <- 0
#         aprovados <- 0
#         para i de 1 ate n faca
#            escreva("Nota do aluno ", i, ": ")
#            leia(nota)
#            soma <- soma + nota
#            se (nota >= 7) entao
#               aprovados <- aprovados + 1
#            fimse
#         fimpara
#         media <- soma / n
#         escreval("Media: ", media)
#         escreval("Aprovados: ", aprovados)
#         escreva("Cadastrar outra turma? (S/N): ")
#         leia(resposta)
#      fimenquanto
#      escreval("Encerrado.")
#   fimalgoritmo
#
# DICA: para deixar a comparação case-insensitive (aceitar "s" e "S"),
#       use resposta.upper() == "S"

# SEU CÓDIGO AQUI:
