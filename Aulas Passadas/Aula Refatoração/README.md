# Aula de refatoração

Material arquivado da aula anterior. É a parte 10 da prática de POO, mas fica
numa pasta própria: foi a primeira aula que não
acrescentou nada ao jogo: no fim da tarde ele fazia exatamente o que fazia de
manhã — mesmas fases, mesmos inimigos, mesmas mensagens na tela. O que mudou
foi a forma.

## Em que ordem

`refatoracao.pdf`, do começo ao fim. Cada capítulo segue o mesmo ritmo:

```
problema  ->  explicação  ->  exemplo  ->  exemplo  ->  exercício
```

Os capítulos são cinco: a linha do dano copiada em dois arquivos vira
`calcular_dano`; os números mudos ganham nome; o `if/elif` do menu vira tabela;
a guarda repetida em quatro habilidades sobe para a mãe como método modelo; e
os quatro atributos de bônus viram a classe `BonusTemporario`.

Os exemplos completos tratam de boletim escolar, carrinho de supermercado,
elevador, semáforo, caixa eletrônico, catraca de ônibus, impressora, empréstimo
de biblioteca, ar-condicionado e estoque de farmácia.

## A regra que valeu

**Refatorar é mudar a forma sem mudar o comportamento.** Mesma entrada, mesma
saída — foi a única medida de sucesso do dia. Sem teste automatizado, a
conferência foi no olho, um capítulo por vez.

## Código-base daquela aula

A pasta [`codigo-base/`](codigo-base/) contém os quatro arquivos que estavam em
`Hoje/Codigo Base` no começo da aula de refatoração: os seis inimigos já
decidem, e nada foi refatorado ainda. É o ponto de partida da parte 10.

**O resultado** da refatoração — os mesmos quatro arquivos com os cinco
capítulos aplicados — está em [`../Aula Testes Automatizados/codigo-base/`](../Aula%20Testes%20Automatizados/codigo-base/)
e também em `Hoje/Codigo Base`. Serve de gabarito desta aula.

## Uma errata do PDF

Na etapa 3 do exercício 6, a linha de exemplo aparece assim:

```python
if not self.bonus_ataque.ativo() and self.vida < VIDA_BAIXA_ORC:
```

Está abreviada. `VIDA_BAIXA_ORC` é a fração `0.5` criada no capítulo 2, então a
comparação correta é contra a vida máxima:

```python
if not self.bonus_ataque.ativo() and self.vida < self.vida_maxima * VIDA_BAIXA_ORC:
```

Escrito como está no PDF, o Orc entraria em fúria com 49 de vida em vez de com
metade dela — o que muda o comportamento do jogo e viola a regra do dia.

## O que ficou valendo

| Nome | Onde | O que é |
|---|---|---|
| `calcular_dano()` | `Personagem` | O sorteio do dano num lugar só. Devolve valor, não imprime. |
| `usar_habilidade(alvo)` | `Personagem` | O roteiro da habilidade: guarda, efeito, recarga. As filhas só preenchem os buracos. |
| `mensagem_de_recarga()` / `turnos_de_recarga()` / `efeito_da_habilidade(alvo)` | filhas | Os três buracos. O Dragão só escreve dois: a recarga dele é o padrão da mãe. |
| `BonusTemporario` | `personagem.py` | Quanto e por quantos turnos. Não sabe a que atributo pertence. |
| `ACOES` | `main.py` | O menu do turno como tabela, no formato `"tecla": (rótulo, função)`. |
| `recompensar(jogador, fase)` | `main.py` | As quatro coisas que acontecem ao vencer uma fase. |

A palavra `habilidade_especial` não existe mais em nenhum arquivo.

## Aula seguinte

Testes automatizados, em [`../Aula Testes Automatizados/`](../Aula%20Testes%20Automatizados/)
— que começa exatamente do resultado desta aula, e prova com código o que aqui
foi conferido no olho.
