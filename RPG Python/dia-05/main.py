from personagem import Personagem


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

        turno_do_jogador(jogador, inimigo)

        if inimigo.esta_vivo():
            inimigo.atacar(jogador)

    if jogador.esta_vivo():
        print("Vitória contra", inimigo.nome)
        return True

    print("Você foi derrotado")
    return False


def main():
    jogador = Personagem("Thoric", 100, 15, 5, 2)

    inimigos = [
        Personagem("Goblin", 40, 8, 2, 0),
        Personagem("Orc", 70, 12, 4, 0),
        Personagem("Troll", 100, 16, 6, 0),
    ]

    for inimigo in inimigos:
        venceu = combate(jogador, inimigo)
        if not venceu:
            break

    if jogador.esta_vivo():
        print("Todos os inimigos foram derrotados")


if __name__ == "__main__":
    main()
