# Parte 9: a inteligência do inimigo

Material arquivado da aula anterior. O inimigo deixa de só atacar e passa a
escolher o que fazer no turno dele, através do método `agir` — que separa
**decidir** uma ação de **executar** uma ação.

## Em que ordem

`ia-de-inimigo.pdf`, do começo ao fim. Cada capítulo segue o mesmo ritmo:

```
problema  ->  explicação  ->  exemplo  ->  exemplo  ->  exercício
```

Os capítulos são cinco: nasce o `agir` sem nada mudar no jogo; o Goblin lê o
próprio estado; Orc e Troll reaproveitam os bônus temporários que já existiam;
o inimigo ganha habilidade especial e recarga sem infraestrutura nova; e um
inimigo novo entra sem que o combate saiba.

Os exemplos completos tratam de termostato, loja, celular, carro, banco,
veículos, cafeteira e pagamentos. As decisões do RPG não aparecem prontas.

## Código-base daquela aula

A pasta [`codigo-base/`](codigo-base/) contém os quatro arquivos que estavam em
`Hoje/Codigo Base` no começo da aula de IA de inimigo. Eles já possuem
habilidades especiais e recarga, mas nenhum inimigo decide nada — exatamente o
ponto do qual os alunos partiram naquele dia.

O código-base da aula seguinte, com os seis inimigos decidindo, está na pasta
`Hoje/Codigo Base` enquanto refatoração for a aula atual.

## A regra que valeu

**A IA decide, mas não inventa estado.** Nenhuma classe de inimigo ganhou
atributo novo: vida, vida máxima e recarga já estavam lá, e toda decisão saiu de
combinar o que existia.

## O contrato que ficou valendo

| Nome | Onde | O que é |
|---|---|---|
| `agir(self, alvo)` | `Personagem` | A promessa comum: escolher uma ação. A base ataca; as filhas decidem. |
| `atacar` / `defender` | `Personagem` | Quem executa. O `agir` nunca faz o trabalho, só escolhe quem faz. |
| `combate` | `main.py` | Chama `inimigo.agir(jogador)` e não sabe qual inimigo é. |

Nesta aula o jogo passou de quatro para seis fases: a Cripta Antiga (Esqueleto)
e o Penhasco dos Ventos (Harpia) entraram para dar palco às decisões novas.
