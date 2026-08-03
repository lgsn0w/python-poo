# Hoje: fases e progressão

O assunto de hoje é uma continuação direta da composição: o jogo ganha uma
sequência de **fases**, cada uma guardando o seu inimigo e o seu prêmio.

Até agora o prêmio de cada luta era decidido num `if` dentro do laço principal.
Hoje essa decisão sai do `if` e passa a morar dentro da fase — a mesma ideia de
"tem um" que já apareceu na mochila do personagem, aplicada num lugar novo.

## Em que ordem

1. **`fases-e-progressao.pdf`**, o único documento de hoje. Tem cinco
   capítulos curtos, cada um com um checkpoint. Leia, escreva o código, rode, e
   siga para o próximo capítulo quando o resultado bater com o que está na
   página.

## O que você precisa antes de começar

O jogo da aula passada rodando, com quatro arquivos:

```
rpg/
  personagem.py     com Personagem, _vida, curar e o inventario
  itens.py           com Item, PocaoDeVida, Bomba e Inventario
  classes.py         Guerreiro, Mago, Goblin, Orc, Troll, Dragao
  main.py            o menu, o combate e a mochila
```

Nenhum arquivo novo entra hoje. A classe de hoje, `Fase`, mora dentro do
`main.py`.

Se o seu jogo não estiver funcionando, a teoria de composição está em
[`../Aulas Passadas/teoria-poo/parte-c-composicao/`](../Aulas%20Passadas/teoria-poo/parte-c-composicao/),
e os exercícios que constroem o `itens.py` estão em
[`../Aulas Passadas/pratica-poo/parte-3-composicao-e-inventario/`](../Aulas%20Passadas/pratica-poo/parte-3-composicao-e-inventario/).

## Aulas anteriores

Todo o material das aulas passadas está em
[`../Aulas Passadas/`](../Aulas%20Passadas/), com a mesma organização de
sempre.
