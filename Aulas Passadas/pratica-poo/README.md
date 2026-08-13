# Prática de POO

Material para você seguir sozinho, no seu ritmo.

Você começa com o RPG que a turma escreveu no
[`dia-05-rpg-completo/`](../dia-05-rpg-completo/) e termina com um jogo de
verdade: com escolha de personagem, inimigos diferentes e um chefe final.

A teoria destes conceitos está em [`teoria-poo/`](../teoria-poo/). Aqui você
escreve o código.

## As partes

| Parte | Assunto |
|---|---|
| [Parte 1](parte-1-heranca-e-polimorfismo/) | Herança e polimorfismo |
| [Parte 2](parte-2-encapsulamento-e-o-jogo/) | Encapsulamento e o jogo |
| [Parte 3](parte-3-composicao-e-inventario/) | Composição e o inventário |
| [Parte 4](parte-4-fases-e-progressao/) | Fases e progressão |
| [Parte 5](parte-5-mais-itens/) | Mais itens |
| [Parte 6](parte-6-progressao/) | Progressão |
| [Parte 7](parte-7-efeitos-temporarios/) | Efeitos temporários |
| [Parte 8](parte-8-habilidades-especiais/) | Habilidades especiais |
| [Parte 9](parte-9-ia-de-inimigo/) | IA de inimigo |
| Parte 10 | Refatoração — fica em [`../Aula Refatoração/`](../Aula%20Refatora%C3%A7%C3%A3o/) |

Termine cada parte inteira antes de abrir a seguinte. A parte atual fica em
`Hoje/`, não aqui.

A partir da parte 4, cada pasta tem um `codigo-base/` com os arquivos do começo
daquela aula. Se você perdeu o fio em algum ponto, é de lá que dá para retomar
sem refazer tudo.

## Antes de começar

Você precisa ter estes dois arquivos funcionando:

| Arquivo | Como deve estar |
|---|---|
| `personagem.py` | A classe `Personagem` do Dia 5, sem alterações |
| `main.py` | O combate rodando, do jeito que ficou no Dia 5 |

Se você perdeu algum, os dois estão em
[`dia-05-rpg-completo/`](../dia-05-rpg-completo/).

Durante a Parte 1 você vai criar um terceiro arquivo, o `classes.py`, e o
`personagem.py` fica intocado do começo ao fim. Na Parte 2 você passa a editar o
`personagem.py` também, e o documento avisa para fazer uma cópia de segurança
antes.

## Como o material funciona

Leia, escreva o código, rode, e compare o resultado com o que está na página.

Você vai encontrar quatro tipos de caixa:

| Caixa | O que fazer |
|---|---|
| **Checkpoint** | Marca o fim de uma etapa. Diz o que o seu código precisa fazer nesse ponto. |
| **Teste** | Um código curto para rodar. Se o resultado bater com o da página, você entendeu. Se não bater, a caixa explica o que provavelmente aconteceu. |
| **Leia a fonte** | Uma pergunta cuja resposta está na documentação oficial do Python, em português. Procure e responda. |
| **Extra** | Opcional. Fica no anexo B de cada PDF. |

Não pule os testes. Tem código que roda e mesmo assim está errado por dentro, e os
testes existem justamente para pegar esse caso.

## Sobre os extras

Os extras são para quem terminou um checkpoint antes e quer ir mais fundo.

**Pular todos os extras não te deixa para trás em nada.** Eles não são cobrados, e
nenhum capítulo depende deles. Um extra pode depender de outro extra, e quando
depende está escrito embaixo do título.

## Como rodar o seu jogo

Dentro da pasta onde estão os seus arquivos:

```
python3 main.py
```

Não precisa instalar nada além do Python.

## Quando travar

1. **Leia a mensagem de erro inteira.** A última linha diz o que aconteceu, e a
   linha acima dela costuma dizer onde.
2. **Procure no anexo A** do PDF que você está fazendo. Ele lista os erros mais
   comuns, com a mensagem exata e o que fazer.
3. **Confira a indentação.** Método que ficou fora da classe é a causa mais comum
   de "escrevi o código e nada acontece".
4. **Peça ajuda.** Travar não quer dizer que você errou feio. Quer dizer que
   chegou na parte difícil.
