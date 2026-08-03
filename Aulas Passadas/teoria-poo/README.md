# Teoria de POO

Material de teoria de Orientação a Objetos, feito depois do projeto de RPG. Cada
parte fica em uma pasta, com o documento principal em PDF, a fonte em Markdown, e
um README com explicações mais simples.

## Partes

- [Parte A: conceitos que você já usa](parte-a-conceitos-que-voce-ja-usa/) dá nome
  ao que o aluno já usou no RPG: abstração, encapsulamento, estado e
  comportamento, e objeto que fala com objeto. Não ensina sintaxe nova.
- [Parte B: herança e polimorfismo](parte-b-heranca-e-polimorfismo/) apresenta
  conteúdo novo: herança, `super()`, sobrescrita, polimorfismo, e quando não usar
  herança. Usa Guerreiro, Mago e Ladino.
- [Parte C: composição](parte-c-composicao/) apresenta a outra metade da
  orientação a objetos: a relação "tem um". Item, poção, bomba, inventário,
  `__str__` e `@property`.

Ordem sugerida: Parte A, depois Parte B, depois Parte C. Quem já reconhece
atributo e método pode começar direto pela Parte B.

## Como gerar os PDFs

Os PDFs são gerados a partir dos arquivos `.md` com o script `md2pdf.py`, sem
dependências externas:

```
python3 md2pdf.py parte-a-conceitos-que-voce-ja-usa/parte-a-conceitos-que-voce-ja-usa.md \
                  parte-a-conceitos-que-voce-ja-usa/parte-a-conceitos-que-voce-ja-usa.pdf
```

O script aceita um subconjunto de Markdown: títulos `#`, `##` e `###`, listas com
`-` e `1.`, blocos ` ```python `, `>` para notas, `---` para separador, `**negrito**`
e `` `código` ``. Mantenha o Markdown dentro desse subconjunto.
