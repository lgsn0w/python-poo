from classes import Dragao, Esqueleto, Goblin, Guerreiro, Harpia, Mago, Orc, Troll
from itens import AnelDeProtecao, Bomba, ElixirDeFuria, PocaoDeVida, TonicoDePedra

CLASSES = {
    "1": Guerreiro,
    "2": Mago,
}

DESCANSO_ENTRE_FASES = 50


class Fase:
    def __init__(self, nome, descricao, inimigo, premio):
        self.nome = nome
        self.descricao = descricao
        self.inimigo = inimigo
        self.premio = premio


def escolher_personagem():
    print("Escolha o seu personagem:")
    for tecla, classe in CLASSES.items():
        print(tecla, "-", classe.__name__)

    escolha = input("Opção: ")
    while escolha not in CLASSES:
        print("Opção inválida")
        escolha = input("Opção: ")

    nome = input("Nome: ")
    return CLASSES[escolha](nome)


def turno_do_jogador(jogador, inimigo):
    def atacar(jogador, inimigo):
        jogador.atacar(inimigo)

    def defender(jogador, inimigo):
        jogador.defender()

    def mochila(jogador, inimigo):
        abrir_mochila(jogador, inimigo)

    def habilidade(jogador, inimigo):
        jogador.usar_habilidade(inimigo)

    ACOES = {
        "1": ("Atacar", atacar),
        "2": ("Defender", defender),
        "3": ("Abrir a mochila", mochila),
        "4": ("Usar habilidade especial", habilidade),
    }

    print()
    for tecla, (rotulo, _) in ACOES.items():
        print(tecla, "-", rotulo)

    escolha = input("Escolha: ")

    if escolha not in ACOES:
        print("Opção inválida")
        return

    rotulo, acao = ACOES[escolha]
    acao(jogador, inimigo)


def abrir_mochila(jogador, inimigo):
    if jogador.inventario.esta_vazio():
        print("A mochila esta vazia")
        return

    jogador.inventario.listar()
    escolha = input("Qual item? (0 para voltar) ")

    if not escolha.isdigit() or escolha == "0":
        return

    item = jogador.inventario.tirar(int(escolha))
    if item is None:
        print("Esse item nao existe")
        return

    item.usar(jogador, inimigo)


def combate(jogador, inimigo):
    while jogador.esta_vivo() and inimigo.esta_vivo():
        jogador.mostrar_status()
        inimigo.mostrar_status()

        jogador.iniciar_turno()
        turno_do_jogador(jogador, inimigo)

        if inimigo.esta_vivo():
            inimigo.iniciar_turno()
            inimigo.agir(jogador)

    if jogador.esta_vivo():
        print("Vitória contra", inimigo.nome)
        return True

    print("Você foi derrotado")
    return False


def recompensar(jogador, fase):
    jogador.subir_nivel()

    jogador.curar(DESCANSO_ENTRE_FASES)
    print(jogador.nome, "descansa e recupera", DESCANSO_ENTRE_FASES, "de vida")

    jogador.inventario.adicionar(fase.premio)
    print(fase.inimigo.nome, "deixou cair:", fase.premio)


def main():
    jogador = escolher_personagem()

    fases = [
        Fase("Floresta Sombria", "Um Goblin salta na sua frente.", Goblin(), PocaoDeVida()),
        Fase("Trilha da Montanha", "Um Orc bloqueia o caminho.", Orc(), ElixirDeFuria()),
        Fase("Ponte Quebrada", "Um Troll ronca embaixo da ponte.", Troll(), TonicoDePedra()),
        Fase("Cripta Antiga", "Um Esqueleto se levanta do chão.", Esqueleto(), Bomba()),
        Fase("Penhasco dos Ventos", "Uma Harpia mergulha do alto.", Harpia(), AnelDeProtecao()),
        Fase("Covil do Dragão", "O Dragão Ancião desperta.", Dragao(), PocaoDeVida()),
    ]

    for fase in fases:
        print("\n==", fase.nome, "==")
        print(fase.descricao)

        venceu = combate(jogador, fase.inimigo)
        if not venceu:
            print("Fim de jogo.")
            return

        recompensar(jogador, fase)

    print("\nVocê derrotou todos os inimigos. Fim.")


if __name__ == "__main__":
    main()
