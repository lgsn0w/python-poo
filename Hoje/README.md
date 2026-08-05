# Hoje: progressão

O assunto de hoje é uma continuação direta de mais itens: o personagem passa
a melhorar sozinho, ganhando ataque, defesa e vida máxima a cada fase
vencida.

Até agora vencer uma fase só rendia descanso e um prêmio guardado na
mochila. Hoje a vitória também deixa o personagem mais forte na hora — sem o
jogador precisar usar nada.

## Em que ordem

1. **`progressao.pdf`**, o único documento de hoje. Primeiro a explicação —
   três métodos de melhora (`melhorar_ataque`, `melhorar_defesa`,
   `melhorar_vida_maxima`), o método que os junta (`subir_nivel`), e onde ele
   é chamado no jogo. Depois, nas últimas páginas do mesmo PDF, seis
   exercícios curtos, cada um com um checkpoint e um teste, para você fazer
   sozinho.

## Por que "progressão" e não outra coisa

No fim da aula de mais itens, ficou uma promessa: `melhorar_ataque`. Hoje ela
vira realidade, junto de mais dois métodos do mesmo formato e um quarto que
junta os três. Não entra nenhuma ideia nova de orientação a objetos — entra
a prática de escrever métodos que mudam o estado do próprio objeto, e de
decidir quando chamá-los durante o jogo.

## O que você precisa antes de começar

O jogo com fases e itens já funcionando, com quatro arquivos:

```
rpg/
  personagem.py     com Personagem, _vida, curar, ataque e defesa
  itens.py           com Item, PocaoDeVida, Bomba, PocaoDeForca, AnelDeProtecao e Inventario
  classes.py         Guerreiro, Mago, Goblin, Orc, Troll, Dragao
  main.py            a classe Fase, a lista fases, o menu e o combate
```

Nenhum arquivo novo entra hoje — os métodos de hoje moram dentro do
`personagem.py` que já existe, e a chamada nova é uma linha dentro do laço
que já existe no `main.py`.

## A pasta Codigo Base

Se o seu jogo não estiver funcionando, ou se você não terminou a aula
passada a tempo, pegue os quatro arquivos prontos em
[`Codigo Base/`](Codigo%20Base/) e comece de lá. Esse código já tem a Poção
de força e o Anel de proteção prontos, e os dois já são prêmio de fase — é
exatamente o ponto onde a aula de ontem devia ter terminado. Usar ele não é
cola: a aula de hoje é sobre progressão, não sobre itens, então não faz
sentido perder tempo hoje consertando um problema de ontem.

## Se travar na teoria de mais atrás

- `@property`, e por que `self.vida_maxima = x` de fora da classe não
  funciona, está em
  [`../Aulas Passadas/teoria-poo/parte-c-composicao/`](../Aulas%20Passadas/teoria-poo/parte-c-composicao/).
- Os exercícios que construíram a Poção de força e o Anel de proteção estão
  em
  [`../Aulas Passadas/pratica-poo/parte-5-mais-itens/`](../Aulas%20Passadas/pratica-poo/parte-5-mais-itens/).
- A aula de fases, completa, está em
  [`../Aulas Passadas/pratica-poo/parte-4-fases-e-progressao/`](../Aulas%20Passadas/pratica-poo/parte-4-fases-e-progressao/).

## Aulas anteriores

Todo o material das aulas passadas está em
[`../Aulas Passadas/`](../Aulas%20Passadas/), com a mesma organização de
sempre.
