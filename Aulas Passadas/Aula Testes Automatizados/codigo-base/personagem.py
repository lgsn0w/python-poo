import random

from itens import Inventario, PocaoDeVida

LADOS_DO_DADO = 20
ROLAGEM_MINIMA_PARA_ACERTAR = 5
VARIACAO_DO_DANO = 3

TURNOS_DE_RECARGA_PADRAO = 3


class BonusTemporario:
    """Guarda quanto e por quantos turnos. Nao sabe a que atributo pertence."""

    def __init__(self):
        self.quantidade = 0
        self.turnos = 0

    def ativo(self):
        return self.turnos > 0

    def comecar(self, quantidade, turnos):
        self.quantidade = quantidade
        self.turnos = turnos

    def passar_turno(self):
        """Devolve True apenas no turno em que o bonus acaba."""
        if self.turnos == 0:
            return False
        self.turnos -= 1
        return self.turnos == 0

    def limpar(self):
        self.quantidade = 0


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, pocoes):
        self.nome = nome
        self._vida = vida
        self._vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.defendendo = False
        self.nivel = 1
        self.bonus_ataque = BonusTemporario()
        self.bonus_defesa = BonusTemporario()
        self._recarga_habilidade = 0

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
        print("\n", self.nome, "- Nível", self.nivel)
        print("Vida:", self._vida, "/", self._vida_maxima)
        print("Mochila:", self.inventario.quantidade(), "item(ns)")

        if self.habilidade_disponivel():
            print("Habilidade: disponível")
        else:
            print("Habilidade: faltam", self._recarga_habilidade, "turno(s)")

    def esta_vivo(self):
        return self._vida > 0

    def iniciar_turno(self):
        self.defendendo = False

        if self.bonus_ataque.passar_turno():
            self.ataque -= self.bonus_ataque.quantidade
            self.bonus_ataque.limpar()
            print(self.nome, "sente o ataque voltar ao normal")

        if self.bonus_defesa.passar_turno():
            self.defesa -= self.bonus_defesa.quantidade
            self.bonus_defesa.limpar()
            print(self.nome, "sente a defesa voltar ao normal")

        if self._recarga_habilidade > 0:
            self._recarga_habilidade -= 1

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

    def calcular_dano(self):
        return random.randint(self.ataque - VARIACAO_DO_DANO,
                              self.ataque + VARIACAO_DO_DANO)

    def atacar(self, alvo):
        rolagem = random.randint(1, LADOS_DO_DADO)

        if rolagem < ROLAGEM_MINIMA_PARA_ACERTAR:
            print(self.nome, "errou o ataque")
            return

        dano = self.calcular_dano()
        alvo.receber_dano(dano)
        print(self.nome, "causou", dano, "de dano")

    def defender(self):
        self.defendendo = True
        print(self.nome, "preparou a defesa")

    def agir(self, alvo):
        self.atacar(alvo)

    def habilidade_disponivel(self):
        return self._recarga_habilidade == 0

    def iniciar_recarga(self, turnos):
        self._recarga_habilidade = turnos

    def usar_habilidade(self, alvo):
        """O roteiro, igual para todos. As filhas preenchem os buracos."""
        if not self.habilidade_disponivel():
            print(self.mensagem_de_recarga() + ".", "Faltam",
                  self._recarga_habilidade, "turno(s)")
            return

        self.efeito_da_habilidade(alvo)
        self.iniciar_recarga(self.turnos_de_recarga())

    def mensagem_de_recarga(self):
        return "A habilidade ainda se prepara"

    def turnos_de_recarga(self):
        return TURNOS_DE_RECARGA_PADRAO

    def efeito_da_habilidade(self, alvo):
        print(self.nome, "não possui habilidade especial")

    def melhorar_ataque(self, quantidade):
        self.ataque += quantidade

    def melhorar_defesa(self, quantidade):
        self.defesa += quantidade

    def melhorar_vida_maxima(self, quantidade):
        self._vida_maxima += quantidade
        self._vida += quantidade

    def aplicar_bonus_ataque_temporario(self, quantidade, turnos):
        if self.bonus_ataque.ativo():
            self.ataque -= self.bonus_ataque.quantidade

        self.ataque += quantidade
        self.bonus_ataque.comecar(quantidade, turnos)
        print(self.nome, "sente o ataque aumentar por um tempo")

    def aplicar_bonus_defesa_temporario(self, quantidade, turnos):
        if self.bonus_defesa.ativo():
            self.defesa -= self.bonus_defesa.quantidade

        self.defesa += quantidade
        self.bonus_defesa.comecar(quantidade, turnos)
        print(self.nome, "sente a defesa aumentar por um tempo")

    def subir_nivel(self):
        self.nivel += 1
        self.melhorar_ataque(4)
        self.melhorar_defesa(2)
        self.melhorar_vida_maxima(20)
        print(self.nome, "subiu para o nível", self.nivel)
