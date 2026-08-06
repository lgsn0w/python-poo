# Hoje: efeitos temporários

O assunto de hoje é uma continuação direta de progressão: nem todo bônus
deveria durar para sempre. Hoje um bônus aprende a contar os próprios turnos
e a ir embora sozinho, sem ninguém precisar lembrar de desfazer nada.

## Em que ordem

1. **`efeitos-temporarios.pdf`**, a explicação, para acompanhar no telão.
   Mostra `aplicar_bonus_ataque_temporario`, o gancho dentro de
   `iniciar_turno` que desfaz o bônus quando o prazo acaba, e o Elixir de
   fúria, o primeiro item que usa o padrão novo. Este documento já mostra o
   código pronto — ele não é para ser seguido sozinho, é para ser explicado.
2. **`efeitos-temporarios-exercicios.pdf`**, depois. Seis exercícios curtos:
   construir o método de ataque, ligar ele ao `iniciar_turno`, construir o
   elixir, colocar ele numa fase, e então repetir o padrão inteiro sozinho
   para defesa. Ao contrário do primeiro documento, este não dá o código
   pronto — só diz o que cada peça precisa ter, e traz um teste no fim de
   cada exercício para você conferir sozinho se bateu.

## Por que "efeitos temporários" e não outra coisa

No fim da aula de progressão, ficou uma pergunta dentro de um método que já
existia: `iniciar_turno` já reseta `defendendo` no começo de cada turno — e
se um bônus tivesse que "acabar" ali também? Hoje não entra nenhuma ideia
grande de orientação a objetos; entra a prática de fazer um objeto lembrar
do próprio estado ao longo de vários turnos, e de desfazer sozinho o que ele
mesmo aplicou.

## O que você precisa antes de começar

O jogo com progressão já funcionando, com quatro arquivos:

```
rpg/
  personagem.py     com Personagem, nivel, subir_nivel, melhorar_ataque/defesa/vida_maxima
  itens.py           com Item, PocaoDeVida, Bomba, PocaoDeForca, AnelDeProtecao e Inventario
  classes.py         Guerreiro, Mago, Goblin, Orc, Troll, Dragao
  main.py            a classe Fase, a lista fases, o menu, o combate, subir_nivel a cada vitória
```

Nenhum arquivo novo entra hoje — os métodos moram dentro do `personagem.py`
que já existe, o item novo mora dentro do `itens.py` que já existe, e a
troca de prêmio é uma linha dentro da lista `fases` que já existe no
`main.py`.

## A pasta Codigo Base

Se o seu jogo não estiver funcionando, ou se você não terminou a aula
passada a tempo, pegue os quatro arquivos prontos em
[`Codigo Base/`](Codigo%20Base/) e comece de lá. Esse código já tem
`subir_nivel` funcionando e chamado a cada vitória — é exatamente o ponto
onde a aula de ontem devia ter terminado. Usar ele não é cola: a aula de
hoje é sobre efeitos temporários, não sobre progressão, então não faz
sentido perder tempo hoje consertando um problema de ontem.

## Se travar na teoria de mais atrás

- `@property`, encapsulamento e por que o personagem protege o próprio
  estado estão em
  [`../Aulas Passadas/teoria-poo/parte-c-composicao/`](../Aulas%20Passadas/teoria-poo/parte-c-composicao/).
- Os exercícios que construíram `melhorar_ataque`, `melhorar_defesa` e
  `subir_nivel` estão em
  [`../Aulas Passadas/pratica-poo/parte-6-progressao/`](../Aulas%20Passadas/pratica-poo/parte-6-progressao/).
- Os exercícios que construíram a Poção de força e o Anel de proteção estão
  em
  [`../Aulas Passadas/pratica-poo/parte-5-mais-itens/`](../Aulas%20Passadas/pratica-poo/parte-5-mais-itens/).

## Aulas anteriores

Todo o material das aulas passadas está em
[`../Aulas Passadas/`](../Aulas%20Passadas/), com a mesma organização de
sempre.
