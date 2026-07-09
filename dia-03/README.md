# Jogo RPG — projeto da turma

Um jogo de batalha por turnos, construído em aula, aplicando o que já foi visto de Orientação a Objetos em
Python. Este projeto começa do zero — as classes e exercícios anteriores (`02-classes`, `03-exercicios`)
foram treino; o código daqui pra frente é o jogo de verdade.

## Objetivo

Construir, em etapas, um jogo de batalha por turnos entre personagens (`Guerreiro`, `Mago`) e adversários,
usando só o que for aprendido em aula, na ordem em que for aprendido. Nenhuma etapa usa um conceito antes de
ele ter sido explicado.

## Como o projeto está dividido

O jogo é construído em fases. Cada fase soma sobre a anterior — nada é jogado fora.

### Fase 1 — Fundamentos (atual)
Classes com atributos completos (`vida`, `ataque`, `defesa`, `pocoes`) e três ações básicas:

- `atacar(alvo)` — causa dano em outro personagem
- `defender()` — reduz o próximo dano recebido pela metade
- `usar_pocao()` — recupera vida, com número limitado de usos

Ainda sem laço de jogo automático. As ações são testadas chamando os métodos manualmente, na ordem que
quiser, pra confirmar que cada peça funciona antes de automatizar qualquer coisa.

### Fase 2 — Jogo jogável
- `input()` pra escolher personagem e ação a cada turno
- `random` pra variar o dano do inimigo e sortear o tipo de ataque (normal / crítico / fraco)
- Um laço `while` juntando tudo — o jogo roda sozinho, turno após turno, até alguém vencer

### Fase 3 — Mais conteúdo
- Múltiplos inimigos em sequência, não só um
- Limite real de itens (poções) ao longo de uma partida inteira, não só um combate

### Fase 4 — Movimento (futuro)
- Personagem se movendo por um mapa
- Ainda não definido em detalhe — vem depois que a Fase 2 e 3 estiverem sólidas

## Estrutura de arquivos (planejada)

```
04-jogo/
├── guerreiro.py
├── mago.py
├── main.py
└── README.md
```

Cada classe no seu próprio arquivo; `main.py` importa e organiza tudo, seguindo o mesmo padrão já visto no
guia de "várias classes num main".

## Como rodar

```
python main.py
```

(válido a partir da Fase 2, quando o jogo ganha um ponto de entrada interativo de verdade)

## Status

Fase 1 em andamento.
