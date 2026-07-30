# Hoje: composição

O assunto de hoje é **composição**: um objeto guardar outro objeto dentro de si.

Até agora você usou herança, que é a relação "é um". Hoje entra a outra metade,
a relação "tem um". O seu RPG ganha uma mochila, e os itens ganham comportamento
próprio.

## Em que ordem

1. **`teoria-composicao.pdf`**, leia primeiro. Explica a ideia e mostra por que
   fazer uma poção herdar de `Personagem` dá errado sem dar erro. Cada seção
   termina com perguntas.
2. **`exercicios-composicao.pdf`**, depois. Onze exercícios e seis checkpoints.
   Cada um diz o que fazer, em qual arquivo, e como saber se deu certo.

## O que você precisa antes de começar

O jogo da aula passada rodando, com três arquivos:

```
rpg/
  personagem.py     com _vida, curar e iniciar_turno
  classes.py        Guerreiro, Mago, Goblin, Orc, Troll, Dragao
  main.py           o menu de personagem e o combate
```

Se o seu não estiver funcionando, pegue os três em
[`Ajuda Extra/Codigo Base/`](Ajuda%20Extra/Codigo%20Base/) e comece de lá.

Hoje entra **um** arquivo novo, o `itens.py`, e passam a ser quatro. Nenhum
outro.

## A pasta Ajuda Extra

Você não precisa dela para fazer a aula. Ela tem:

- **`Codigo Base/`**, os três arquivos prontos do ponto onde a aula de hoje
  começa. Use se o seu jogo quebrou.
- **`ajuda-composicao.md`**, os pontos difíceis explicados outra vez, com
  palavras mais simples. Leia quando travar em alguma parte da teoria.
- **`teoria-composicao.md`**, o mesmo texto do PDF da teoria, em formato de
  texto, para quem preferir ler assim ou quiser editar.

## Aulas anteriores

Todo o material das aulas passadas está em
[`../Aulas Passadas/`](../Aulas%20Passadas/), com a mesma organização de sempre.
