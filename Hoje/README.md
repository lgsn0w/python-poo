# Hoje: testes automatizados

Ontem o jogo mudou de forma sem mudar de comportamento, e a conferência foi
toda no olho: jogar, chegar na fase certa, provocar a situação certa e olhar a
tela. Cinco vezes, uma por capítulo.

Hoje o computador passa a fazer essa conferência. Uma vez escrita, ela custa
meio segundo e não esquece de nada.

## Em que ordem

Use **`testes-automatizados.pdf`** do começo ao fim. Cada capítulo segue sempre
o mesmo ritmo:

```
problema  ->  explicação  ->  exemplo  ->  exemplo  ->  exercício
```

Os capítulos são cinco, em ordem de dificuldade:

1. **A primeira afirmação** — a palavra `assert`, e a ideia de que silêncio é
   aprovação.
2. **Um arquivo só de testes** — com doze afirmações soltas, a primeira que
   falha esconde as outras onze. Entra o `unittest`, com `setUp` e placar.
3. **Testar o que sorteia** — o dano muda toda vez. Afirmar a propriedade,
   fixar a semente, ou injetar o sorteio: três saídas, em ordem de preferência.
4. **Testar o que imprime** — quase tudo no jogo termina em `print`, e `print`
   não se afirma. Testar pelo efeito no estado.
5. **O teste que pega a regra** — as três regras que quase morreram ontem
   (erros 5, 6 e 7 do anexo A da refatoração), e o teste que você precisa ver
   falhar antes de aceitar.

Os exemplos completos tratam de cofrinho, conversor de temperatura, placar de
vôlei, máquina de salgadinhos, dado de tabuleiro, rifa, agenda de consultas,
validação de senha, estoque de padaria e pedido de lanchonete.

O PDF tem ainda três anexos: nove erros que você vai ver, oito extras opcionais
e o checklist de entrega.

## A regra do dia

**O jogo não sabe que os testes existem.** Nenhum `import testes` aparece nos
outros quatro arquivos. A seta aponta num sentido só: `testes.py` conhece o
jogo, o jogo não conhece os testes.

## Nada de arquivo novo — menos um

Ontem a regra era que nenhum arquivo novo entrava. Hoje entra exatamente um,
`testes.py`, e ele não tem regra de jogo nenhuma dentro.

```
rpg/
  personagem.py     Personagem e BonusTemporario
  classes.py        Guerreiro, Mago e os seis inimigos
  itens.py          poções, elixires e o inventário
  main.py           fases, inventário, combate e progressão
  testes.py         NOVO
```

No fim do dia o arquivo tem 24 testes ou mais, e `python testes.py` termina em
`OK`.

## O que você precisa antes de começar

O jogo **já refatorado**. Os testes do material chamam `calcular_dano`,
`usar_habilidade` e `bonus_ataque.ativo()` — três coisas que só existem depois
da parte 10.

## A pasta Codigo Base

Se o seu jogo não chegou ao fim da refatoração, pegue os quatro arquivos em
[`Codigo Base/`](Codigo%20Base/). Eles são o jogo de ontem com os cinco
capítulos aplicados, e servem também de **gabarito da parte 10**: se você quiser
comparar a sua refatoração com uma solução possível, é ali.

É uma solução possível, não a única. O que importa é que a saída na tela seja a
mesma — e essa parte foi conferida: três partidas completas, com a mesma
semente e as mesmas teclas, produzem saída idêntica byte a byte à do código
anterior à refatoração.

Usar o código-base não entrega a atividade de hoje. Ele apenas evita perder a
aula consertando conteúdos anteriores.

## Conceitos retomados

- **Encapsulamento:** o capítulo 5 mostra que testar a implementação
  (`bonus_ataque.turnos`) prende o teste ao lado de dentro, e testar a regra
  (o ataque subiu 6) não prende.
- **Composição:** a `BonusTemporario` é testada sem criar nenhum `Personagem`.
  A frase que você escreveu ontem — "não sabe a que atributo pertence" — vira
  uma coisa que dá para provar.
- **Separar decidir de executar:** o `agir` da parte 9 e o `media()` com
  `return` da parte 10 voltam no capítulo 4, agora com um motivo novo.

## Aula anterior

O material de refatoração foi arquivado em
[`../Aulas Passadas/Aula Refatoração/`](../Aulas%20Passadas/Aula%20Refatora%C3%A7%C3%A3o/).

Todo o restante está em [`../Aulas Passadas/`](../Aulas%20Passadas/).
