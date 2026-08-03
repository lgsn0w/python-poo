# Parte C: composição

Esta pasta tem a teoria da Parte C.

- `parte-c-composicao.pdf` é o documento principal. Leia ele primeiro.
- `parte-c-composicao.md` é o mesmo texto, em Markdown, para editar.
- Este README explica os pontos difíceis outra vez, com palavras mais simples.
  Use ele quando travar em alguma parte do PDF.

Faça a Parte B antes desta. A Parte C parte do princípio de que você já sabe o
que é herança e o que é `super()`.

## Ideia geral em uma frase

Nem toda relação entre classes é "é um". A maioria é "tem um", e para essa você
não usa herança: você guarda o objeto dentro do outro.

## Se você travou em "por que não herdar"

Herança funciona mesmo quando está errada. Esse é o problema.

Se você escrever `class Pocao(Personagem)`, o Python não reclama. A poção ganha
`atacar`, `defender`, `esta_vivo` e uma mochila. Nada disso dá erro na tela. O
programa roda, e está errado por dentro.

Por isso a regra não é técnica, é uma frase. Diga em voz alta: "poção é um
personagem". Se soar estranho, não herde.

## Se você travou em "é um" contra "tem um"

Duas frases, duas ferramentas.

- "Guerreiro **é um** Personagem": verdade. Herança.
- "Personagem **tem uma** mochila": verdade. Composição.
- "Mochila **é um** Personagem": falso. Nem pense.

Um truque: herança é para a **mesma coisa** agindo diferente. Composição é para
juntar **coisas diferentes**.

Guerreiro e Mago são a mesma coisa (personagens) com comportamentos diferentes.
Personagem e mochila são coisas diferentes que andam juntas.

## Se você travou em "composição"

Composição não tem sintaxe nova. É um atributo, igual aos que você já escreve.

A diferença é o que está guardado dentro dele:

    self.nome = nome              # guarda um texto
    self.vida = vida              # guarda um numero
    self.inventario = Inventario()  # guarda um OBJETO

Como é um objeto, ele tem métodos. Por isso `jogador.inventario.adicionar(x)`
funciona: pegue o jogador, pegue a mochila dele, mande a mochila guardar.

## Se você travou em "delegação"

O personagem não sabe como uma lista funciona. Ele só sabe pedir.

Errado: `self.inventario._itens.append(pocao)`, mexendo na lista dos outros.

Certo: `self.inventario.adicionar(pocao)`, pedindo.

É a mesma ideia do encapsulamento da Parte 2, agora entre dois objetos
diferentes em vez de dentro de um só.

## Se você travou em "polimorfismo de novo"

Na Parte B, `inimigo.atacar()` fazia coisas diferentes conforme o inimigo.

Aqui, `item.usar(dono, inimigo)` faz coisas diferentes conforme o item. A poção
cura quem usou. A bomba fere o outro. Mesma chamada, mesmos parâmetros, efeitos
opostos.

O que mudou é só onde: agora são objetos que não são personagens. É a prova de
que polimorfismo não era um truque do combate.

## Se você travou em `__str__`

`__str__` responde uma pergunta: "como você vira texto?".

Você não chama ele na mão. Você escreve `print(item)`, e o Python chama por você.
É igual ao `__init__`, que roda sozinho quando o objeto nasce.

Cuidado com dois detalhes. O nome tem dois underscores de cada lado. E dentro
dele você usa `return`, não `print`. Se usar `print`, o método devolve `None` e o
Python reclama.

## Se você travou em `@property`

Na Parte 2 você trocou `vida` por `_vida` e fechou a porta inteira. Mas o
problema nunca foi ler, foi escrever.

`@property` deixa ler sem deixar escrever:

    @property
    def vida(self):
        return self._vida

Depois disso, `print(goblin.vida)` funciona e `goblin.vida = -999` continua
dando erro.

O detalhe bonito: quem usa não muda nada. Continua escrevendo `goblin.vida`, sem
parênteses, como se fosse atributo comum. Você trocou o interior sem quebrar
ninguém de fora.

## Glossário rápido

- composição: um objeto guardar outro objeto dentro de si.
- "é um": a relação de herança. Guerreiro é um Personagem.
- "tem um": a relação de composição. Personagem tem uma mochila.
- delegação: chamar o método do objeto guardado em vez de mexer nos dados dele.
- `__str__`: método especial que diz como o objeto vira texto.
- `@property`: transforma um método em algo que se lê como atributo.

## Como usar este material

Leia o PDF na ordem das seções. Não pule a Seção 1: ela mostra a poção que ataca,
e é o incômodo que justifica a parte inteira.

Depois, faça os exercícios em `pratica-poo/parte-3-composicao-e-inventario/`.
