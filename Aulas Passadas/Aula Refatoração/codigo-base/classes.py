import random

from personagem import Personagem


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 120, 18, 8, 2)
        self.dano_golpe = 12
        self.recarga_golpe = 3

    def atacar(self, alvo):
        dano = random.randint(self.ataque - 3, self.ataque + 3)
        alvo.receber_dano(dano)
        print(self.nome, "atacou sem falhar e causou", dano, "de dano")

    def habilidade_especial(self, alvo):
        if not self.habilidade_disponivel():
            print("O golpe esmagador ainda se recompõe. Faltam",
                  self._recarga_habilidade, "turno(s)")
            return

        dano = self.ataque + self.dano_golpe
        alvo.receber_dano(dano)
        self.iniciar_recarga(self.recarga_golpe)
        print(self.nome, "desferiu o Golpe Esmagador com força", dano)


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 70, 10, 3, 4)
        self.dano_magico = 22
        self.recarga_bola_de_fogo = 4

    def defender(self):
        super().defender()
        self.curar(10)
        print(self.nome, "recuperou 10 de vida")

    def habilidade_especial(self, alvo):
        if not self.habilidade_disponivel():
            print("A bola de fogo ainda se forma. Faltam",
                  self._recarga_habilidade, "turno(s)")
            return

        alvo.receber_dano(self.dano_magico + alvo.defesa)
        self.iniciar_recarga(self.recarga_bola_de_fogo)
        print(self.nome, "lançou a Bola de Fogo causando", self.dano_magico,
              "de dano mágico, ignorando a defesa")


class Goblin(Personagem):
    def __init__(self):
        super().__init__("Goblin", 40, 8, 2, 0)

    def agir(self, alvo):
        if self.vida < self.vida_maxima * 0.3:
            self.defender()
            return

        self.atacar(alvo)


class Orc(Personagem):
    def __init__(self):
        super().__init__("Orc", 70, 12, 4, 0)

    def agir(self, alvo):
        if self._turnos_bonus_ataque == 0 and self.vida < self.vida_maxima * 0.5:
            print("O Orc entra em fúria")
            self.aplicar_bonus_ataque_temporario(6, 3)
            return

        self.atacar(alvo)


class Troll(Personagem):
    def __init__(self):
        super().__init__("Troll", 100, 16, 6, 0)

    def agir(self, alvo):
        if self._turnos_bonus_defesa == 0 and self.vida < self.vida_maxima * 0.4:
            print("O Troll endurece a pele")
            self.aplicar_bonus_defesa_temporario(4, 3)
            return

        self.atacar(alvo)

    def atacar(self, alvo):
        rolagem = random.randint(1, 20)
        if rolagem < 9:
            print("O Troll errou feio")
            return
        dano = random.randint(self.ataque, self.ataque + 10)
        alvo.receber_dano(dano)
        print("O Troll acertou um golpe de", dano)


class Esqueleto(Personagem):
    def __init__(self):
        super().__init__("Esqueleto", 55, 11, 3, 0)

    def receber_dano(self, quantidade):
        print("Os ossos rangem")
        super().receber_dano(quantidade)

    def habilidade_especial(self, alvo):
        if not self.habilidade_disponivel():
            print("Os ossos ainda se recompõem. Faltam",
                  self._recarga_habilidade, "turno(s)")
            return

        self.curar(15)
        self.iniciar_recarga(4)
        print("O Esqueleto remonta os próprios ossos e recupera 15 de vida")

    def agir(self, alvo):
        if self.habilidade_disponivel() and self.vida < self.vida_maxima * 0.5:
            self.habilidade_especial(alvo)
            return

        self.atacar(alvo)


class Harpia(Personagem):
    def __init__(self):
        super().__init__("Harpia", 60, 13, 2, 0)

    def agir(self, alvo):
        if alvo.defendendo:
            print("A Harpia sobe e espera a guarda baixar")
            self.defender()
            return

        self.atacar(alvo)


class Dragao(Personagem):
    def __init__(self):
        super().__init__("Dragão Ancião", 110, 14, 4, 0)

    def habilidade_especial(self, alvo):
        if not self.habilidade_disponivel():
            print("O sopro ainda se acumula. Faltam",
                  self._recarga_habilidade, "turno(s)")
            return

        dano = self.ataque + 8
        print("O Dragão solta um sopro de fogo!")
        alvo.receber_dano(dano + alvo.defesa)
        self.iniciar_recarga(3)
        print("O sopro causou", dano, "de dano e ignorou a defesa")

    def agir(self, alvo):
        if self.habilidade_disponivel():
            self.habilidade_especial(alvo)
            return

        self.atacar(alvo)
