# POO em Python · Dia 4

`input()`, `random`, e o laço que junta tudo — o jogo passa a rodar do começo ao fim.

## 1. O que é novo hoje

Só duas ferramentas. Tudo o mais (classes, `__init__`, métodos, `if/elif/else`, `while`) já foi visto.

### `input()`

`input()` **sempre devolve uma string**, mesmo que a pessoa digite um número.

```python
resposta = input("Digite algo: ")
print(type(resposta))  # <class 'str'>
```

Quando você precisa comparar com um número, converta antes com `int()`:

```python
escolha = int(input("Digite 1 ou 2: "))
if escolha == 1:
    print("opção 1")
```

Sem o `int()`, `escolha == 1` é `False` porque `"1" != 1` em Python.

Quando comparar com **texto** (tipo `"atacar"`), não precisa converter — `input()` já devolve string.

### `random`

Importar no topo do arquivo, antes de qualquer outra coisa:

```python
import random
```

O método mais usado hoje:

```python
numero = random.randint(a, b)  # inteiro entre a e b, incluindo os dois
```

Exemplo:

```python
rolagem = random.randint(1, 20)
print("Você rolou:", rolagem)
```

Cada chamada sorteia um valor diferente — é isso que vai fazer o dano variar e o ataque poder errar.

---

## 2. Dicas por exercício

### Exercício 1 — Escolher personagem

- `input()` pede a escolha, `int()` converte antes de comparar
- `if/elif/else` cobre: opção 1, opção 2, e qualquer outra coisa
- No `else`, crie o personagem padrão — o jogo não pode travar por entrada inválida
- O objeto `jogador` deve existir em todos os caminhos

### Exercício 2 — Turno do jogador

- Aqui a resposta é texto (`"atacar"`, `"defender"`, `"pocao"`) — sem `int()`
- Cada `elif` chama **um método que já existe** na classe — não escreva lógica nova aqui
- `else` pega qualquer outra entrada e deixa o turno passar sem erro

### Exercício 3 — Dano variável

- `import random` vai no topo do arquivo onde suas classes estão
- Dentro de `atacar()`, troque `self.ataque` por `random.randint(mínimo, máximo)`
- Os limites são derivados de `self.ataque` — pense: quanto acima e quanto abaixo faz sentido?

### Exercício 4 — Chance de acerto (d20)

- Role o d20 **antes** de calcular o dano
- O `if/else` decide: abaixo de certo valor → errou, caso contrário → aplica o dano do Exercício 3
- Se errar, `receber_dano()` **não é chamado** — só uma mensagem

### Exercício 5 — Laço completo

- `while` com **duas condições**: jogador vivo **e** inimigo vivo
- Dentro do laço: turno do jogador (Exercício 2), depois cheque se inimigo ainda vive antes de ele atacar
- Depois do laço: só um dos dois sobrou vivo — a condição do `if` diz qual

### Exercício 6 — Vários inimigos (desafio)

- Uma lista de inimigos, não um único objeto
- O laço do Exercício 5 roda de novo para cada inimigo — use um `for` externo
- Poções **não resetam** entre batalhas — `self.pocoes` continua do estado anterior
- Cheque se o jogador ainda está vivo antes de passar pro próximo inimigo

---

## 3. Erros comuns

**Comparar string com número sem converter:**
```python
# errado — escolha é "1", não 1
if escolha == 1:

# certo
if int(escolha) == 1:
# ou converta na hora do input()
escolha = int(input("..."))
```

**Usar `int()` quando a entrada é texto:**
```python
# errado — "atacar" não vira int, lança ValueError
acao = int(input("..."))

# certo — comparação de texto não precisa de int()
acao = input("...")
if acao == "atacar":
```

**Esquecer o `import random`:**
```python
# NameError: name 'random' is not defined
dano = random.randint(5, 10)

# certo — import no topo, antes das classes
import random
```

**Chamar `receber_dano()` mesmo quando o ataque errou:**

No Exercício 4, o `if/else` protege isso — só o caminho de acerto chama `receber_dano()`.

---

## Arquivos

| Arquivo | O que é |
|---|---|
| `04_exercicios.pdf` | Lista de exercícios do Dia 4 |
| `Codigos/` | Pasta pra enviar o código resolvido |
