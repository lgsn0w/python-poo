# Parte B: herança e polimorfismo

Esta pasta tem a teoria da Parte B.

- `parte-b-heranca-e-polimorfismo.pdf` é o documento principal. Leia ele primeiro.
- `parte-b-heranca-e-polimorfismo.md` é o mesmo texto, em Markdown, para editar.
- Este README explica os pontos difíceis outra vez, com palavras mais simples.
  Use ele quando travar em alguma parte do PDF.

A Parte B tem conteúdo novo. Faça a Parte A antes só se você ainda não sabe o que
é atributo e método. Se isso já está claro, pode começar direto pela Parte B.

## Ideia geral em uma frase

Herança deixa você escrever o que é comum uma vez só, na classe-mãe, e escrever só
a diferença em cada classe-filha.

## Se você travou em "por que herança"

Hoje Goblin, Orc e Troll são a mesma classe `Personagem`. Muda só o número.

O problema aparece quando os tipos precisam agir diferente. Um Mago ataca com
magia. Um Ladino ataca com crítico. Sem herança, você enche o método `atacar` de
`if self.tipo == ...`. Cada tipo novo mexe nesse `if` e arrisca quebrar os outros.

Herança separa isso. O que é igual fica na mãe. O que é diferente fica em cada
filha.

## Se você travou em "classe-mãe e classe-filha"

`class Guerreiro(Personagem):` quer dizer "o Guerreiro é um Personagem".

O Guerreiro ganha de graça tudo que o `Personagem` tem: `vida`, `receber_dano`,
`defender`, `esta_vivo`, `mostrar_status`. Você não reescreve nada disso.

Regra do "é um". Se a frase "X é um Personagem" for verdadeira, X pode ser uma
classe-filha. Guerreiro é um Personagem. Mago é um Personagem. Mochila não é um
Personagem, então mochila não herda.

## Se você travou em "super().__init__()"

`super()` chama a classe-mãe.

Dentro do `__init__` da filha, `super().__init__(...)` manda o `Personagem` montar
`nome`, `vida`, `ataque`, `defesa` e `pocoes`. A filha só precisa passar os
números dela. Depois, a filha pode acrescentar um atributo próprio, como
`self.mana` no Mago.

Ordem importa. Chame `super().__init__(...)` primeiro. Só depois acrescente os
atributos da filha.

Se você esquecer o `super().__init__(...)`, o objeto nasce sem `vida`, sem `nome`,
sem nada da mãe. Aí `mostrar_status()` quebra.

## Se você travou em "sobrescrita"

Sobrescrever é a filha escrever um método com o mesmo nome de um método da mãe. A
versão da filha passa a valer para os objetos daquele tipo.

O Mago escreve o próprio `atacar`. Quando você chama `mago.atacar(inimigo)`, roda
o `atacar` do Mago, não o da mãe.

Cuidado com o nome. O nome precisa ser idêntico. `def Atacar` com A maiúsculo não
sobrescreve nada. `def atacar_mago` também não. Nos dois casos o Python não avisa,
e o objeto continua usando o `atacar` herdado.

## Duas formas de sobrescrever

Existe uma diferença entre as Seções 4 e 5 do PDF. Ela confunde muita gente.

- Trocar por completo (Seção 4). O `atacar` do Mago não tem nada a ver com o
  ataque normal. Ele escreve tudo de novo e não chama `super()`.
- Aproveitar e somar (Seção 5). O `defender` do Paladino quer o defender normal e
  mais uma cura. Ele chama `super().defender()` primeiro, e depois acrescenta a
  cura.

Pergunta que resolve a dúvida: a filha quer o comportamento da mãe mais alguma
coisa, ou quer um comportamento totalmente diferente? Se é "mais alguma coisa",
use `super()`. Se é "diferente", não use.

## Se você travou em "polimorfismo"

O laço de combate chama `inimigo.atacar(jogador)`. Essa linha não muda nunca.

O inimigo pode ser Goblin, Mago ou Ladino. Cada um responde do próprio jeito. O
laço não pergunta o tipo. O objeto certo faz a ação certa sozinho.

Resultado prático. Para criar um tipo novo, você escreve uma classe nova. Você não
mexe no laço de combate. O código antigo fica intacto.

## Onde olhar quando algo dá errado

- A Seção 7 do PDF junta os erros mais comuns ao herdar. Leia ela como uma lista
  de conferência.
- A Seção 9 do PDF traz o código completo das três classes-filhas e um combate
  passo a passo. Use ela como exemplo pronto para comparar com o seu código.

## Glossário rápido

- herança: criar uma classe a partir de outra e aproveitar o que já existe.
- classe-mãe: a classe de onde os métodos vêm. Aqui, `Personagem`.
- classe-filha: a classe que herda. Aqui, `Guerreiro`, `Mago`, `Ladino`.
- `super()`: uma forma de chamar a classe-mãe de dentro da filha.
- sobrescrita: a filha redefine um método com o mesmo nome da mãe.
- polimorfismo: a mesma chamada roda comportamentos diferentes conforme o objeto.

## Como usar este material

Leia o PDF na ordem das seções. Não pule a Seção 1, porque ela mostra o problema
que a herança resolve. Quando travar, volte aqui na parte com o mesmo nome. Depois
escreva você mesmo as classes `Guerreiro`, `Mago` e `Ladino` e rode o combate.
