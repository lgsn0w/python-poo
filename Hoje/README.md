# Hoje: a inteligência do inimigo

O assunto de hoje começa com uma coisa que dá para perceber jogando: o jogador
tem quatro opções por turno e o inimigo tem uma. O combate manda o inimigo
atacar, sempre, aconteça o que acontecer.

Hoje o inimigo passa a escolher. E o caminho para isso é separar duas coisas que
estavam grudadas no mesmo lugar: **decidir** uma ação e **executar** uma ação.
Nasce o método `agir`, que só escolhe, e as ações que já existem continuam
fazendo o trabalho delas.

## Em que ordem

Use **`ia-de-inimigo.pdf`** do começo ao fim. Cada capítulo segue sempre o mesmo
ritmo:

```
problema  ->  explicação  ->  exemplo  ->  exemplo  ->  exercício
```

Os capítulos são cinco:

1. **Decidir não é agir** — nasce o `agir`, e nada no jogo muda ainda.
2. **Ler o próprio estado** — o Goblin se defende quando está perdendo.
3. **Decidir sem inventar estado** — Orc e Troll usam os bônus temporários que
   já existem.
4. **O contrato de ontem, do outro lado** — o inimigo ganha habilidade especial
   e recarga sem uma linha nova de infraestrutura.
5. **A prova do desenho** — um inimigo novo entra sem que o combate saiba.

Os exemplos completos tratam de termostato, loja, celular, carro, banco,
veículos, cafeteira e pagamentos. As decisões do RPG não aparecem prontas.

O PDF tem ainda três anexos: erros que você vai ver, extras opcionais e o
checklist de entrega.

## A regra do dia

**A IA decide, mas não inventa estado.** Nenhuma classe de inimigo ganha
atributo novo hoje. Vida, vida máxima e recarga já estão todas lá — toda decisão
interessante sai de combinar o que existe.

## O que você precisa antes de começar

O jogo de sexta, com habilidades especiais funcionando:

```
rpg/
  personagem.py     habilidade_especial e _recarga_habilidade
  itens.py          poções, elixires e o inventário
  classes.py        Guerreiro, Mago, Goblin, Orc, Troll, Esqueleto e Dragao
  main.py           fases, inventário, combate e progressão
```

## A pasta Codigo Base

Se o seu jogo não estiver funcionando ou se você não terminou a aula de sexta,
pegue os quatro arquivos em [`Codigo Base/`](Codigo%20Base/). Eles representam
exatamente o ponto inicial de hoje: progressão, efeitos temporários, habilidades
especiais e recarga já estão prontos, mas nenhum inimigo decide nada.

Usar o código-base não entrega a atividade de hoje. Ele apenas evita perder a
aula consertando conteúdos anteriores.

## Conceitos retomados

- **Herança:** todo inimigo é um `Personagem` e já nasce com o contrato.
- **Sobrescrita:** cada inimigo redefine `agir` com o critério dele.
- **Polimorfismo:** o combate sempre chama `inimigo.agir(jogador)`.
- **Encapsulamento:** a decisão consulta a recarga, mas só o dono a altera.
- **Reúso:** a fúria do Orc usa o mesmo método que o Elixir de Fúria.

## Aula anterior

O material de habilidades especiais foi arquivado em
[`../Aulas Passadas/pratica-poo/parte-8-habilidades-especiais/`](../Aulas%20Passadas/pratica-poo/parte-8-habilidades-especiais/).

Todo o restante está em [`../Aulas Passadas/`](../Aulas%20Passadas/).
