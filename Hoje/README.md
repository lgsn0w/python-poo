# Hoje: habilidades especiais

O assunto de hoje continua a pergunta deixada no fim da aula de efeitos
temporários: o que faria um Guerreiro realmente parecer um Guerreiro e um
Mago realmente parecer um Mago?

As duas classes ganham uma habilidade especial. O menu chama a mesma operação
para qualquer personagem, mas cada classe responde de um jeito diferente. A
habilidade entra em recarga depois do uso, reaproveitando a passagem dos turnos
que a aula de ontem já colocou dentro de `iniciar_turno`.

## Em que ordem

Use **`habilidades-especiais.pdf`** do começo ao fim. A explicação e a prática
ficam intercaladas:

1. explicação sobre o contrato comum e polimorfismo;
2. duas questões práticas;
3. explicação sobre a identidade de Guerreiro e Mago;
4. duas questões práticas;
5. explicação sobre recarga e passagem do tempo;
6. duas questões práticas;
7. explicação sobre integração, status e extensibilidade;
8. duas questões práticas.

O PDF informa assinaturas, parâmetros, atributos possíveis, responsabilidades
e critérios de teste. Os exemplos completos tratam de notificações, fretes e
uma cafeteira. O corpo das habilidades e a solução da recarga do RPG não
aparecem prontos.

O arquivo **`habilidades-especiais.html`** é a fonte editável do PDF.

## O que você precisa antes de começar

O jogo de ontem, com efeitos temporários funcionando:

```
rpg/
  personagem.py     bônus temporários de ataque e defesa dentro de iniciar_turno
  itens.py           ElixirDeFuria e um item temporário de defesa
  classes.py         Guerreiro, Mago, Goblin, Orc, Troll e Dragao
  main.py            fases, inventário, combate e progressão
```

## A pasta Codigo Base

Se o seu jogo não estiver funcionando ou se você não terminou a aula de ontem,
pegue os quatro arquivos em [`Codigo Base/`](Codigo%20Base/). Eles representam
exatamente o ponto inicial de hoje: progressão e efeitos temporários já estão
prontos, mas nenhuma habilidade especial ou recarga foi implementada.

Usar o código-base não entrega a atividade de hoje. Ele apenas evita perder a
aula consertando conteúdos anteriores.

## Conceitos retomados

- **Herança:** Guerreiro e Mago são tipos de `Personagem`.
- **Sobrescrita:** cada filha redefine `habilidade_especial`.
- **Polimorfismo:** o menu sempre chama
  `jogador.habilidade_especial(inimigo)`.
- **Encapsulamento:** o próprio personagem administra sua recarga.
- **Estado ao longo do tempo:** `iniciar_turno` atualiza a espera.

## Aula anterior

O material de efeitos temporários foi arquivado em
[`../Aulas Passadas/pratica-poo/parte-7-efeitos-temporarios/`](../Aulas%20Passadas/pratica-poo/parte-7-efeitos-temporarios/).

Todo o restante está em [`../Aulas Passadas/`](../Aulas%20Passadas/).
