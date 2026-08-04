# Hoje: mais itens

O assunto de hoje é uma continuação direta de fases e progressão: o jogo ganha
dois itens novos, uma **Poção de força** e um **Anel de proteção**, os dois
seguindo o mesmo molde da Poção de vida e da Bomba que vocês já têm.

## Em que ordem

1. **`mais-itens.pdf`**, o único documento de hoje. Tem dez páginas curtas:
   uma recapitulação, e depois cada item novo em três partes — o contexto, o
   código comparado lado a lado com um item que já existe, e o porquê daquilo
   funcionar. Termina mostrando os dois itens virando prêmio de fase.

## Por que "mais itens" e não outra coisa

Vocês já aprenderam o padrão inteiro: toda classe de item tem um
`usar(self, dono, inimigo)`, e é só isso que o resto do jogo (a mochila, o
menu, a fase) precisa saber para usar qualquer item, sem `if` nenhum
perguntando qual é. Hoje não entra nenhuma ideia nova de orientação a
objetos — entra a prática de aplicar esse padrão duas vezes, sozinhos, até
ele virar automático. É o mesmo motivo de terem existido a Poção de vida
*e* a Bomba na aula passada: um exemplo só nunca prova que o padrão
generaliza.

## O que você precisa antes de começar

O jogo com fases já funcionando, com quatro arquivos:

```
rpg/
  personagem.py     com Personagem, _vida, curar, ataque e defesa
  itens.py           com Item, PocaoDeVida, Bomba e Inventario
  classes.py         Guerreiro, Mago, Goblin, Orc, Troll, Dragao
  main.py            a classe Fase, a lista fases, o menu e o combate
```

Nenhum arquivo novo entra hoje — os dois itens vão dentro do `itens.py` que
já existe, do lado da `PocaoDeVida` e da `Bomba`.

## A pasta Codigo Base

Se o seu jogo de fases não estiver funcionando, ou se você não terminou a
aula passada a tempo, pegue os quatro arquivos prontos em
[`Codigo Base/`](Codigo%20Base/) e comece de lá. Esse código já tem a classe
`Fase` funcionando, com as quatro fases de exemplo — é exatamente o ponto
onde a aula de ontem devia ter terminado. Usar ele não é cola: a aula de
hoje é sobre os itens, não sobre fases, então não faz sentido perder tempo
hoje consertando um problema de ontem.

## Se travar na teoria de mais atrás

- Composição (por que um item não herda de `Personagem`) está em
  [`../Aulas Passadas/teoria-poo/parte-c-composicao/`](../Aulas%20Passadas/teoria-poo/parte-c-composicao/).
- Os exercícios que construíram o `itens.py` pela primeira vez estão em
  [`../Aulas Passadas/pratica-poo/parte-3-composicao-e-inventario/`](../Aulas%20Passadas/pratica-poo/parte-3-composicao-e-inventario/).
- A aula de fases de ontem, completa, está em
  [`../Aulas Passadas/pratica-poo/parte-4-fases-e-progressao/`](../Aulas%20Passadas/pratica-poo/parte-4-fases-e-progressao/).

## Aulas anteriores

Todo o material das aulas passadas está em
[`../Aulas Passadas/`](../Aulas%20Passadas/), com a mesma organização de
sempre.
