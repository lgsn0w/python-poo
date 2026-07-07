# POO em Python · Dia 2
# Exercícios — resolva cada um no espaço indicado.
# Referência rápida nos comentários de cada exercício.


# ─────────────────────────────────────────────────────────────
# PARTE 1 — Criando classes e chamando métodos
# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 1 · PERSONAGEM COMPLETO
#
# Crie a classe Personagem com __init__(self, nome, vida, ataque).
# Adicione um método mostrar_status() que classifica a vida:
#   >= 70  → "saudavel"
#   >= 30  → "ferido"
#   >  0   → "critico"
#   else   → "morto"
# Crie dois personagens com valores diferentes e chame mostrar_status() em cada um.


# SEU CÓDIGO AQUI:


# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 2 · MÉTODO QUE MUDA O ESTADO
#
# Ainda na classe Personagem, adicione receber_dano(quantidade):
#   - subtrai quantidade de self.vida
#   - se self.vida ficar abaixo de 0, deixa em 0
# Aplique dano duas vezes num personagem, chamando mostrar_status() depois de cada uma.


# SEU CÓDIGO AQUI:


# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 3 · CLASSE NOVA + FOR DENTRO DO MÉTODO
#
# Crie uma classe Inimigo com __init__(self, nome, tipo).
# Adicione atacar_varias_vezes(vezes): usa um for pra imprimir
# "nome ataca!" o número de vezes indicado.
# Crie uma lista com 3 inimigos e percorra com um for por fora,
# chamando atacar_varias_vezes(2) em cada um.


# SEU CÓDIGO AQUI:


# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 4 · MÉTODO QUE DEVOLVE UM VALOR
#
# Ainda em Personagem, crie calcular_dano_total(tipo_ataque).
# Recebe uma string: "normal", "critico" ou "fraco".
# Devolve (return) self.ataque multiplicado por:
#   "critico" → x2
#   "fraco"   → x0.5
#   "normal"  → x1
# Guarde o resultado numa variável e só depois imprima.


# SEU CÓDIGO AQUI:


# ─────────────────────────────────────────────────────────────
# PARTE 2 — Classes específicas: Guerreiro e Mago
# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 5 · GUERREIRO · WHILE
#
# Crie a classe Guerreiro com __init__(self, nome, energia).
# Adicione atacar_com_espada():
#   - while self.energia > 0: imprime mensagem de golpe e subtrai 1
#   - quando energia chegar a 0: imprime que o guerreiro está cansado


# SEU CÓDIGO AQUI:


# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 6 · MAGO · WHILE
#
# Crie a classe Mago com __init__(self, nome, mana).
# Adicione conjurar_ate_acabar():
#   - while self.mana >= 10: conjura um feitiço (imprime e subtrai 10)
#   - usa um contador separado pra somar cada feitiço conjurado
#   - quando sair do while: imprime o total de feitiços


# SEU CÓDIGO AQUI:


# ─────────────────────────────────────────────────────────────

# EXERCÍCIO 7 · DESAFIO · FUNÇÃO POR FORA DAS CLASSES
#
# Escreva uma função duelo(guerreiro, mago) — fora de qualquer classe.
# Recebe um objeto Guerreiro e um objeto Mago.
# Compara guerreiro.energia com mago.mana usando if/elif/else
# e imprime quem "venceria" o duelo (ou empate).
# Chame a função passando objetos que você criou acima.


# SEU CÓDIGO AQUI:
