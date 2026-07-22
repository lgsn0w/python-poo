import random


class Personagem:
    """Representa um participante do combate.

    Esta classe é a base que a turma já estudou.
    As atividades novas começam a partir desta classe.
    """

    def __init__(self, nome, vida, ataque, defesa, pocoes):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.pocoes = pocoes
        self.defendendo = False

    def mostrar_status(self):
        print("\n", self.nome)
        print("Vida:", self.vida, "/", self.vida_maxima)
        print("Poções:", self.pocoes)

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, quantidade):
        dano_real = quantidade - self.defesa

        if self.defendendo:
            dano_real = dano_real // 2
            self.defendendo = False

        dano_real = max(0, dano_real)
        self.vida = max(0, self.vida - dano_real)

    def atacar(self, alvo):
        rolagem = random.randint(1, 20)

        if rolagem < 5:
            print(self.nome, "errou o ataque")
            return

        dano = random.randint(self.ataque - 3, self.ataque + 3)
        alvo.receber_dano(dano)
        print(self.nome, "causou", dano, "de dano")

    def defender(self):
        self.defendendo = True
        print(self.nome, "preparou a defesa")

    def usar_pocao(self):
        if self.pocoes == 0:
            print("Sem poções")
            return

        if self.vida == self.vida_maxima:
            print("Vida cheia")
            return

        self.vida = min(self.vida + 25, self.vida_maxima)
        self.pocoes -= 1
        print(self.nome, "usou uma poção")
