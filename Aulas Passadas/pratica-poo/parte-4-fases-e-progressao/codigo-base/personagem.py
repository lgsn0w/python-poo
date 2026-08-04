import random

from itens import Inventario, PocaoDeVida


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, pocoes):
        self.nome = nome
        self._vida = vida
        self._vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.defendendo = False

        self.inventario = Inventario()
        for _ in range(pocoes):
            self.inventario.adicionar(PocaoDeVida())

    @property
    def vida(self):
        return self._vida

    @property
    def vida_maxima(self):
        return self._vida_maxima

    def __str__(self):
        return f"{self.nome} ({self._vida}/{self._vida_maxima})"

    def mostrar_status(self):
        print("\n", self.nome)
        print("Vida:", self._vida, "/", self._vida_maxima)
        print("Mochila:", self.inventario.quantidade(), "item(ns)")

    def esta_vivo(self):
        return self._vida > 0

    def iniciar_turno(self):
        self.defendendo = False

    def curar(self, quantidade):
        if quantidade <= 0:
            return
        self._vida = min(self._vida + quantidade, self._vida_maxima)

    def receber_dano(self, quantidade):
        dano_real = quantidade - self.defesa

        if self.defendendo:
            dano_real = dano_real // 2

        dano_real = max(0, dano_real)
        self._vida = max(0, self._vida - dano_real)

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
