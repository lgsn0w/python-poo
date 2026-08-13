import random

from personagem import Personagem

# --- Guerreiro ---
DANO_DO_GOLPE = 12
RECARGA_DO_GOLPE = 3

# --- Mago ---
DANO_MAGICO = 22
RECARGA_DA_BOLA_DE_FOGO = 4
CURA_DA_DEFESA_DO_MAGO = 10

# --- Goblin ---
VIDA_BAIXA_GOBLIN = 0.3

# --- Orc ---
VIDA_BAIXA_ORC = 0.5
FORCA_DA_FURIA = 6
DURACAO_DA_FURIA = 3

# --- Troll ---
VIDA_BAIXA_TROLL = 0.4
FORCA_DO_ENDURECIMENTO = 4
DURACAO_DO_ENDURECIMENTO = 3
ROLAGEM_MINIMA_DO_TROLL = 9
DANO_EXTRA_DO_TROLL = 10

# --- Esqueleto ---
VIDA_BAIXA_ESQUELETO = 0.5
CURA_DOS_OSSOS = 15
RECARGA_DOS_OSSOS = 4

# --- Dragão ---
DANO_EXTRA_DO_SOPRO = 8


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 120, 18, 8, 2)

    def atacar(self, alvo):
        dano = self.calcular_dano()
        alvo.receber_dano(dano)
        print(self.nome, "atacou sem falhar e causou", dano, "de dano")

    def mensagem_de_recarga(self):
        return "O golpe esmagador ainda se recompõe"

    def turnos_de_recarga(self):
        return RECARGA_DO_GOLPE

    def efeito_da_habilidade(self, alvo):
        dano = self.ataque + DANO_DO_GOLPE
        alvo.receber_dano(dano)
        print(self.nome, "desferiu o Golpe Esmagador com força", dano)


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 70, 10, 3, 4)

    def defender(self):
        super().defender()
        self.curar(CURA_DA_DEFESA_DO_MAGO)
        print(self.nome, "recuperou", CURA_DA_DEFESA_DO_MAGO, "de vida")

    def mensagem_de_recarga(self):
        return "A bola de fogo ainda se forma"

    def turnos_de_recarga(self):
        return RECARGA_DA_BOLA_DE_FOGO

    def efeito_da_habilidade(self, alvo):
        alvo.receber_dano(DANO_MAGICO + alvo.defesa)
        print(self.nome, "lançou a Bola de Fogo causando", DANO_MAGICO,
              "de dano mágico, ignorando a defesa")


class Goblin(Personagem):
    def __init__(self):
        super().__init__("Goblin", 40, 8, 2, 0)

    def agir(self, alvo):
        if self.vida < self.vida_maxima * VIDA_BAIXA_GOBLIN:
            self.defender()
            return

        self.atacar(alvo)


class Orc(Personagem):
    def __init__(self):
        super().__init__("Orc", 70, 12, 4, 0)

    def agir(self, alvo):
        if not self.bonus_ataque.ativo() and self.vida < self.vida_maxima * VIDA_BAIXA_ORC:
            print("O Orc entra em fúria")
            self.aplicar_bonus_ataque_temporario(FORCA_DA_FURIA, DURACAO_DA_FURIA)
            return

        self.atacar(alvo)


class Troll(Personagem):
    def __init__(self):
        super().__init__("Troll", 100, 16, 6, 0)

    def agir(self, alvo):
        if not self.bonus_defesa.ativo() and self.vida < self.vida_maxima * VIDA_BAIXA_TROLL:
            print("O Troll endurece a pele")
            self.aplicar_bonus_defesa_temporario(FORCA_DO_ENDURECIMENTO,
                                                 DURACAO_DO_ENDURECIMENTO)
            return

        self.atacar(alvo)

    def atacar(self, alvo):
        rolagem = random.randint(1, 20)
        if rolagem < ROLAGEM_MINIMA_DO_TROLL:
            print("O Troll errou feio")
            return
        dano = random.randint(self.ataque, self.ataque + DANO_EXTRA_DO_TROLL)
        alvo.receber_dano(dano)
        print("O Troll acertou um golpe de", dano)


class Esqueleto(Personagem):
    def __init__(self):
        super().__init__("Esqueleto", 55, 11, 3, 0)

    def receber_dano(self, quantidade):
        print("Os ossos rangem")
        super().receber_dano(quantidade)

    def mensagem_de_recarga(self):
        return "Os ossos ainda se recompõem"

    def turnos_de_recarga(self):
        return RECARGA_DOS_OSSOS

    def efeito_da_habilidade(self, alvo):
        self.curar(CURA_DOS_OSSOS)
        print("O Esqueleto remonta os próprios ossos e recupera",
              CURA_DOS_OSSOS, "de vida")

    def agir(self, alvo):
        if self.habilidade_disponivel() and self.vida < self.vida_maxima * VIDA_BAIXA_ESQUELETO:
            self.usar_habilidade(alvo)
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

    def mensagem_de_recarga(self):
        return "O sopro ainda se acumula"

    def efeito_da_habilidade(self, alvo):
        dano = self.ataque + DANO_EXTRA_DO_SOPRO
        print("O Dragão solta um sopro de fogo!")
        alvo.receber_dano(dano + alvo.defesa)
        print("O sopro causou", dano, "de dano e ignorou a defesa")

    def agir(self, alvo):
        if self.habilidade_disponivel():
            self.usar_habilidade(alvo)
            return

        self.atacar(alvo)
