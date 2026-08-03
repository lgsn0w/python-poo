from classes import Dragao, Goblin, Guerreiro, Mago, Orc, Troll

CLASSES = {
    "1": Guerreiro,
    "2": Mago,
}


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
    print("\n1 - Atacar")
    print("2 - Defender")
    print("3 - Usar poção")
    escolha = input("Escolha: ")

    if escolha == "1":
        jogador.atacar(inimigo)
    elif escolha == "2":
        jogador.defender()
    elif escolha == "3":
        jogador.usar_pocao()
    else:
        print("Opção inválida")


def combate(jogador, inimigo):
    while jogador.esta_vivo() and inimigo.esta_vivo():
        jogador.mostrar_status()
        inimigo.mostrar_status()

        jogador.iniciar_turno()
        turno_do_jogador(jogador, inimigo)

        if inimigo.esta_vivo():
            inimigo.iniciar_turno()
            inimigo.atacar(jogador)

    if jogador.esta_vivo():
        print("Vitória contra", inimigo.nome)
        return True

    print("Você foi derrotado")
    return False


def main():
    jogador = escolher_personagem()

    inimigos = [Goblin(), Orc(), Troll(), Dragao()]

    for inimigo in inimigos:
        venceu = combate(jogador, inimigo)
        if not venceu:
            print("Fim de jogo.")
            return
        jogador.curar(50)
        print(jogador.nome, "descansa e recupera 50 de vida")

    print("\nVocê derrotou todos os inimigos. Fim.")


if __name__ == "__main__":
    main()
