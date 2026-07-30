# Parte A: conceitos que você já usa

Esta pasta tem a teoria da Parte A.

- `parte-a-conceitos-que-voce-ja-usa.pdf` é o documento principal. Leia ele
  primeiro.
- `parte-a-conceitos-que-voce-ja-usa.md` é o mesmo texto, em Markdown, para
  editar.
- Este README explica os pontos difíceis outra vez, com palavras mais simples.
  Use ele quando travar em alguma parte do PDF.

## Ideia geral em uma frase

Você já programou com objetos. Este material só dá o nome técnico ao que você já
fez no RPG.

## Se você travou em "abstração"

Abstração é dar um apelido a um pedaço de código. Depois você usa o apelido e
esquece o detalhe.

No RPG, `esta_vivo()` é o apelido de `self.vida > 0`. Você pergunta
`if jogador.esta_vivo():` e não precisa lembrar como "estar vivo" é calculado por
dentro.

Fora do código funciona igual. Você diz "ligar o carro". Você não diz "girar a
chave, ativar a bomba, soltar a faísca". "Ligar o carro" é a abstração.

## Se você travou em "encapsulamento"

O objeto é o dono do próprio estado. Ninguém mexe na vida do inimigo por fora.
Todo mundo pede a mudança pelo método `receber_dano`.

Pense no banco. Você não tira dinheiro da conta de alguém com a própria mão. Você
pede no caixa. O caixa segue as regras. O método `receber_dano` é o caixa: ele
desconta a defesa, aplica a metade se estava defendendo, e nunca deixa a vida
ficar negativa.

## Se você travou em "estado e comportamento"

Estado são os dados do objeto. Comportamento são as ações do objeto.

Um truque simples. Se a palavra é um substantivo, é atributo: `vida`, `pocoes`,
`defesa`. Se a palavra é um verbo, é método: `atacar`, `defender`, `usar_pocao`.

## Se você travou em "objeto que fala com objeto"

Na chamada `jogador.atacar(inimigo)`, dois objetos participam.

- `self` é quem chama: o jogador.
- `alvo` é quem recebe: o inimigo.

O jogador não escreve na vida do inimigo. O jogador pede: `alvo.receber_dano(dano)`.
O inimigo aplica o próprio dano. Cada objeto cuida de si.

## Glossário rápido

- classe: o molde.
- objeto: uma peça feita a partir do molde.
- atributo: um dado guardado no objeto.
- método: uma ação que o objeto sabe fazer.
- `self`: o próprio objeto, visto de dentro de um método.
- abstração: dar um nome simples a uma ideia complicada.
- encapsulamento: cada objeto cuida do próprio estado.

## Como usar este material

Leia o PDF de cima a baixo. Quando uma seção não fizer sentido, volte aqui na
parte com o mesmo nome. Depois responda às perguntas do PDF com o `personagem.py`
aberto.
