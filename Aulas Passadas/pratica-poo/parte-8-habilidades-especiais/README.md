# Parte 8: habilidades especiais

Material arquivado da aula anterior. Guerreiro e Mago ganham uma habilidade
própria, o menu chama a mesma operação para qualquer personagem, e a habilidade
entra em recarga depois do uso — reaproveitando a passagem dos turnos que a aula
de efeitos temporários colocou dentro de `iniciar_turno`.

## Em que ordem

`habilidades-especiais.pdf`, do começo ao fim. A explicação e a prática ficam
intercaladas: quatro explicações, cada uma seguida de duas questões práticas.

O PDF informa assinaturas, parâmetros, atributos possíveis, responsabilidades e
critérios de teste. Os exemplos completos tratam de notificações, fretes e uma
cafeteira. O corpo das habilidades e a solução da recarga do RPG não aparecem
prontos.

## Código-base daquela aula

A pasta [`codigo-base/`](codigo-base/) contém os quatro arquivos que estavam em
`Hoje/Codigo Base` no começo da aula de habilidades especiais. Eles já possuem
progressão e efeitos temporários, mas ainda não possuem habilidade especial nem
recarga — exatamente o ponto do qual os alunos partiram naquele dia.

O código-base da aula seguinte, com habilidades e recarga concluídas, está na
pasta `Hoje/Codigo Base` enquanto IA de inimigo for a aula atual.

## O contrato que ficou valendo

| Nome | Onde | O que é |
|---|---|---|
| `habilidade_especial(self, alvo)` | `Personagem` | A promessa comum; as filhas sobrescrevem. |
| `_recarga_habilidade` | `Personagem` | Quantos turnos faltam. Zero significa disponível. |
| `iniciar_turno` | `Personagem` | Quem faz o tempo passar, uma vez por turno. |

Esse contrato continua em uso nas aulas seguintes, inclusive pelos inimigos.
