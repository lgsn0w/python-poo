# Introdução à Programação Orientada a Objetos em Python

Material de apoio para a transição do Portugol para o Python, com foco em **Programação Orientada a Objetos (POO)**.

---

## Estrutura do repositório

```
dia-01-fundamentos-python/   Portugol -> Python: entrada, condições, laços, funções
dia-02-classes-e-objetos/    classes, __init__, atributos, métodos
dia-03-rpg-fase-1/           projeto RPG, fase 1
dia-04-rpg-fase-2/           projeto RPG, fase 2 (input, random, laço)
dia-05-rpg-completo/         RPG completo (personagem.py + main.py)
recapitulacao/               retomada após a pausa (parte 1 e parte 2)
teoria-poo/                  teoria de POO (Parte A e Parte B)
pratica-poo/                 prática de POO (Parte 1 e Parte 2), do RPG ao jogo completo
```

A segunda metade de POO fica em duas pastas que se completam: `teoria-poo/`
apresenta os conceitos, e `pratica-poo/` é o material que o aluno segue sozinho
para aplicá-los, terminando com um jogo jogável.

Cada pasta de dia tem um `README.md` próprio. As respostas do aluno ficam em
`respostas/` dentro de cada dia.

---

## Índice

1. [Portugol → Python: Guia de Tradução](#portugol--python-guia-de-tradução)
2. [Exercícios Traduzidos](#exercícios-traduzidos)
3. [O que é POO?](#o-que-é-poo)
4. [Classes e Objetos](#classes-e-objetos)
5. [Construtor](#construtor)
6. [Atributos](#atributos)
7. [Métodos](#métodos)
8. [Instanciação e Múltiplos Objetos](#instanciação-e-múltiplos-objetos)
9. [Exercícios](#exercícios)
10. [Como executar](#como-executar)

---

## Portugol → Python: Guia de Tradução

### Palavras-chave

| Portugol | Python | Observação |
|---|---|---|
| `algoritmo "Nome"` | — | Python não tem cabeçalho; o arquivo é o programa |
| `var` / `inicio` / `fimalgoritmo` | — | Não existe em Python |
| `escreval(...)` | `print(...)` | `escreva` não quebra linha; `escreval` quebra |
| `escreva(...)` | `print(..., end="")` | Usa `end=""` para não quebrar linha |
| `leia(x)` | `x = input("...")` | Em Python, `input` já exibe uma mensagem |
| `<-` | `=` | Atribuição |
| `inteiro` | `int(...)` | Conversão explícita com `int()` |
| `real` | `float(...)` | Conversão explícita com `float()` |
| `caractere` | `str` | String — padrão do `input()` |
| `//` (comentário) | `#` | Comentário de linha |
| `e` | `and` | Operador lógico E |
| `ou` | `or` | Operador lógico OU |
| `nao` | `not` | Operador lógico NÃO |
| `=` (comparação) | `==` | **Atenção:** em Python `=` é atribuição, `==` é comparação |
| `<>` | `!=` | Diferente |

---

### Estrutura `se / senao`

**Portugol:**
```portugol
se nota >= 7 entao
   escreval("Aprovado")
senao
   escreval("Reprovado")
fimse
```

**Python:**
```python
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

> **Diferenças principais:**
> - `se` → `if`, `senao` → `else`
> - Sem `entao` e sem `fimse` — Python usa `:` e **indentação** para delimitar os blocos
> - A indentação (4 espaços) **não é opcional** — faz parte da sintaxe

**Se encadeado:**

```portugol
// Portugol
se nota >= 9 entao
   escreval("Excelente")
senao
   se nota >= 7 entao
      escreval("Aprovado")
   senao
      escreval("Reprovado")
   fimse
fimse
```

```python
# Python
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

> Python tem `elif` para evitar o aninhamento de `senao se`.

---

### Estrutura `para`

**Portugol:**
```portugol
para i de 1 ate 10 faca
   escreval(i)
fimpara
```

**Python:**
```python
for i in range(1, 11):
    print(i)
```

> **Diferenças principais:**
> - `para i de 1 ate 10` → `for i in range(1, 11)`
> - `range(inicio, fim)` — o fim é **exclusivo**, então `range(1, 11)` vai de 1 a 10
> - Sem `fimpara` — o bloco é delimitado pela indentação

**Tabela `range`:**

| Portugol | Python |
|---|---|
| `para i de 1 ate 5` | `for i in range(1, 6)` |
| `para i de 0 ate 9` | `for i in range(0, 10)` ou `for i in range(10)` |
| `para i de 1 ate n` | `for i in range(1, n + 1)` |

---

### Estrutura `enquanto`

**Portugol:**
```portugol
enquanto (numero <= 0) faca
   escreva("Inválido! Digite novamente: ")
   leia(numero)
fimenquanto
```

**Python:**
```python
while numero <= 0:
    numero = float(input("Inválido! Digite novamente: "))
```

> **Diferenças principais:**
> - `enquanto` → `while`
> - Os parênteses na condição são opcionais em Python
> - Sem `fimenquanto` — indentação delimita o bloco

---

## Exercícios Traduzidos

Os arquivos em `01-traducoes/` contêm as versões Python dos exercícios feitos em Portugol:

| Arquivo | Exercício original | Estrutura |
|---|---|---|
| `soma_media.py` | `algoritmo SomaEMedia.alg` | `para` |
| `tabuada.py` | `algoritmo Tabuada.alg` | `para` |
| `validacao_nota.py` | `pptx-ex1-validacao-nota.alg` | `enquanto` + `se/senao` |
| `soma_sentinela.py` | `pptx-ex2-soma-sentinela.alg` | `enquanto` |
| `menu_calculadora.py` | `pptx-ex3-menu.alg` | `enquanto` + `se/senao` |
| `varias_turmas.py` | `pdf-ex1-varias-turmas.alg` | `enquanto` + `para` + `se` |
| `sistema_pedidos.py` | `pdf-ex2-sistema-pedidos.alg` | `enquanto` + `para` |

---

## O que é POO?

Até agora, nos algoritmos em Portugol, escrevemos **procedimentos**: uma lista de instruções executadas uma após a outra. Isso funciona bem para problemas simples, mas à medida que o programa cresce, fica difícil organizar tudo.

**Programação Orientada a Objetos (POO)** é uma forma de organizar o código em torno de **objetos** — entidades que agrupam **dados** (o que o objeto *é*) e **comportamentos** (o que o objeto *faz*).

### Analogia

Pense em um **aluno**:

| Dado (atributo) | Comportamento (método) |
|---|---|
| nome | apresentar_se() |
| nota | verificar_aprovacao() |
| turma | calcular_media() |

Em vez de ter variáveis soltas (`nome`, `nota`, `turma`) espalhadas pelo código, a POO agrupa tudo isso dentro de um **objeto Aluno**.

---

## Classes e Objetos

Uma **classe** é o molde. Um **objeto** é a coisa criada a partir desse molde.

```
Classe Aluno  →  molde / receita / projeto
   Objeto: aluno1 (nome="Ana", nota=8.5)
   Objeto: aluno2 (nome="Bruno", nota=6.0)
   Objeto: aluno3 (nome="Carla", nota=9.2)
```

Em Python, uma classe é definida com a palavra `class`:

```python
class Aluno:
    pass  # classe vazia por enquanto
```

---

## Construtor

O **construtor** é o método especial chamado automaticamente quando um objeto é criado. Em Python, ele sempre se chama `__init__`.

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
```

> - `self` é uma referência ao próprio objeto que está sendo criado — sempre é o primeiro parâmetro
> - `self.nome = nome` salva o valor recebido dentro do objeto

---

## Atributos

**Atributos** são as variáveis que pertencem a um objeto. Eles guardam o estado do objeto.

```python
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
```

Acessar atributos de fora da classe:

```python
p = Produto("Caderno", 12.50, 100)
print(p.nome)       # Caderno
print(p.preco)      # 12.5
print(p.quantidade) # 100
```

---

## Métodos

**Métodos** são funções definidas dentro de uma classe. Eles descrevem o que um objeto pode *fazer*.

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 7:
            print(f"{self.nome} está Aprovado(a)!")
        else:
            print(f"{self.nome} está Reprovado(a).")

    def apresentar_se(self):
        print(f"Olá, meu nome é {self.nome} e minha nota é {self.nota}.")
```

Chamar métodos:

```python
a = Aluno("Ana", 8.5)
a.apresentar_se()         # Olá, meu nome é Ana e minha nota é 8.5.
a.verificar_aprovacao()   # Ana está Aprovado(a)!
```

> Métodos também recebem `self` como primeiro parâmetro, mas você **não passa** esse valor na chamada — Python faz isso automaticamente.

---

## Instanciação e Múltiplos Objetos

**Instanciar** é criar um objeto a partir de uma classe. Cada objeto é independente e tem seus próprios valores.

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 7:
            return "Aprovado(a)"
        return "Reprovado(a)"


# Criando três objetos da mesma classe
aluno1 = Aluno("Ana", 8.5)
aluno2 = Aluno("Bruno", 6.0)
aluno3 = Aluno("Carla", 9.2)

# Cada um tem seus próprios dados
for aluno in [aluno1, aluno2, aluno3]:
    status = aluno.verificar_aprovacao()
    print(f"{aluno.nome}: {aluno.nota} → {status}")
```

**Saída:**
```
Ana: 8.5 → Aprovado(a)
Bruno: 6.0 → Reprovado(a)
Carla: 9.2 → Aprovado(a)
```

### Objetos numa lista

Trabalhar com listas de objetos é muito comum:

```python
turma = [
    Aluno("Ana", 8.5),
    Aluno("Bruno", 6.0),
    Aluno("Carla", 9.2),
]

soma = 0
for aluno in turma:
    soma += aluno.nota

media = soma / len(turma)
print(f"Média da turma: {media:.2f}")  # Média da turma: 7.90
```

---

## Exercícios

Os exercícios estão em `03-exercicios/exercicios.py`. Cada exercício pede que você crie uma classe e instancie objetos.

---

## Como executar

Qualquer arquivo `.py` pode ser executado com:

```bash
python nome_do_arquivo.py
```

Não é necessário instalar nada além do Python. Baixe em [python.org](https://www.python.org/downloads/).
