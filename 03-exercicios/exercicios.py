# ─────────────────────────────────────────────
#  EXERCÍCIOS — PROGRAMAÇÃO ORIENTADA A OBJETOS
#  Complete cada exercício seguindo as instruções.
#  Não apague os comentários de enunciado.
# ─────────────────────────────────────────────


# ═══════════════════════════════════════════
# EXERCÍCIO 1 — Classe Carro
# ═══════════════════════════════════════════
# Crie uma classe chamada Carro com os atributos:
#   - marca (str)
#   - modelo (str)
#   - ano (int)
#   - velocidade (int) — começa em 0
#
# Métodos:
#   - acelerar(incremento): aumenta a velocidade
#   - frear(decremento): diminui a velocidade (mínimo 0)
#   - exibir_info(): mostra marca, modelo, ano e velocidade atual
#
# Depois de criar a classe, instancie 2 carros diferentes e
# chame os métodos para demonstrar o funcionamento.

# SEU CÓDIGO AQUI:


# ═══════════════════════════════════════════
# EXERCÍCIO 2 — Classe ContaBancaria
# ═══════════════════════════════════════════
# Crie uma classe chamada ContaBancaria com os atributos:
#   - titular (str)
#   - numero (str)
#   - saldo (float) — começa em 0
#
# Métodos:
#   - depositar(valor): adiciona ao saldo (rejeita valores <= 0)
#   - sacar(valor): subtrai do saldo (rejeita se saldo insuficiente)
#   - exibir_extrato(): mostra titular, número e saldo atual
#
# Depois de criar a classe, simule uma sequência de operações:
#   1. Crie uma conta para "Maria"
#   2. Deposite R$ 500,00
#   3. Saque R$ 200,00
#   4. Tente sacar R$ 400,00 (saldo insuficiente)
#   5. Exiba o extrato final

# SEU CÓDIGO AQUI:


# ═══════════════════════════════════════════
# EXERCÍCIO 3 — Classe Turma
# ═══════════════════════════════════════════
# Crie uma classe chamada Turma com os atributos:
#   - nome (str)
#   - alunos (list) — começa vazio
#
# Métodos:
#   - adicionar_aluno(nome, nota): adiciona um dicionário
#     {"nome": nome, "nota": nota} à lista de alunos
#   - calcular_media(): retorna a média das notas
#   - listar_aprovados(): imprime os alunos com nota >= 7
#   - exibir_relatorio(): imprime nome da turma, média e lista de aprovados
#
# Depois de criar a classe, crie uma turma, adicione pelo menos
# 5 alunos e exiba o relatório completo.
#
# DICA: para percorrer a lista de alunos dentro de um método:
#   for aluno in self.alunos:
#       print(aluno["nome"], aluno["nota"])

# SEU CÓDIGO AQUI:


# ═══════════════════════════════════════════
# EXERCÍCIO 4 — Classe Estoque (desafio)
# ═══════════════════════════════════════════
# Crie uma classe chamada Estoque com os atributos:
#   - produtos (list) — lista de objetos Produto
#
# Reutilize (ou redefina aqui) a classe Produto com:
#   - nome, preco, quantidade
#   - valor_total_estoque(): retorna preco * quantidade
#
# Métodos de Estoque:
#   - adicionar_produto(produto): adiciona à lista
#   - valor_total(): retorna a soma dos valores de todos os produtos
#   - produto_mais_caro(): retorna o produto com maior preco
#   - exibir(): imprime todos os produtos com seus valores
#
# Depois de criar as classes, crie um estoque com 4 produtos
# e demonstre todos os métodos.

# SEU CÓDIGO AQUI:
