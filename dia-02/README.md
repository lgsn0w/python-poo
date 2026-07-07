# POO em Python · Dia 2

Construtor, métodos, if/elif/else, while, for e return — tudo dentro de uma classe.

## 1. Relembrando o Dia 1

No Dia 1, a gente criou objetos e preencheu os campos na mão, um por um:

```python
class Personagem:
    nome = ""
    vida = 0
    ataque = 0

thoric = Personagem()
thoric.nome = "Thoric"
thoric.vida = 100
thoric.ataque = 15
```

Funciona — mas repete as mesmas linhas toda vez que um personagem novo nasce. Com dez personagens vira bagunça. O `__init__` resolve isso.

## 2. O construtor `__init__`

`__init__` é um método especial que roda automaticamente assim que a classe é chamada. O objeto já nasce com tudo preenchido:

```python
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque


thoric = Personagem("Thoric", 100, 15)
elara  = Personagem("Elara", 60, 25)
```

As quatro linhas do Dia 1 viram uma. O resultado é idêntico.

`__init__` não é escolha de nome — é reservado pelo Python. Os dois underlines de cada lado (`__`) marcam que é um método especial, reconhecido automaticamente pela linguagem. O apelido informal é *dunder* (de *double underscore*).

## 3. `self`

`self` é sempre o primeiro parâmetro de qualquer método dentro de uma classe. Representa o próprio objeto sendo criado ou usado.

```python
self.nome = nome
```

`nome` à direita é o parâmetro — veio de fora, na chamada `Personagem("Thoric", ...)`. `self.nome` à esquerda é o atributo que vai existir dentro do objeto depois. São duas coisas diferentes com o mesmo nome.

Quando `__init__` roda duas vezes — uma pra `thoric`, outra pra `elara` — `self` é um objeto diferente em cada chamada. É por isso que `thoric.vida` e `elara.vida` podem ter valores diferentes mesmo vindo do mesmo `__init__`.

## 4. Métodos

Um método é uma função dentro da classe. Sempre recebe `self` como primeiro parâmetro:

```python
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def mostrar_status(self):
        if self.vida >= 70:
            situacao = "saudavel"
        elif self.vida >= 30:
            situacao = "ferido"
        elif self.vida > 0:
            situacao = "critico"
        else:
            situacao = "morto"
        print(self.nome, "-", self.vida, "de vida -", situacao)

    def receber_dano(self, quantidade):
        self.vida = self.vida - quantidade
        if self.vida < 0:
            self.vida = 0
```

`mostrar_status` só lê. `receber_dano` recebe um parâmetro além de `self` e muda o estado do objeto.

Chamando:

```python
thoric = Personagem("Thoric", 100, 15)
thoric.mostrar_status()     # Thoric - 100 de vida - saudavel
thoric.receber_dano(50)
thoric.mostrar_status()     # Thoric - 50 de vida - ferido
thoric.receber_dano(60)
thoric.mostrar_status()     # Thoric - 0 de vida - morto
```

`self` não é passado na chamada — Python faz isso automaticamente.

## 5. `while` e `for` dentro de métodos

Tudo que funciona em funções normais funciona dentro de métodos. Não há regras novas:

```python
class Guerreiro:
    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia

    def atacar_com_espada(self):
        while self.energia > 0:
            print(self.nome, "desfere um golpe!")
            self.energia = self.energia - 1
        print(self.nome, "esta cansado.")


class Inimigo:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def atacar_varias_vezes(self, vezes):
        for i in range(vezes):
            print(self.nome, "ataca!")
```

O `while` usa `self.energia` como condição — e `self.energia` diminui dentro do próprio loop. O `for` usa um parâmetro recebido de fora.

## 6. `return` dentro de métodos

Métodos podem devolver valores com `return`, igual a funções comuns:

```python
def calcular_dano_total(self, tipo_ataque):
    if tipo_ataque == "critico":
        return self.ataque * 2
    elif tipo_ataque == "fraco":
        return self.ataque * 0.5
    else:
        return self.ataque
```

```python
dano = thoric.calcular_dano_total("critico")
print(dano)  # 30
```

A diferença entre `return` e `print` dentro do método:
- `print` mostra na tela e descarta o valor
- `return` devolve o valor pra quem chamou, que pode guardar ou usar

## 7. Funções fora das classes

Uma função normal pode receber objetos como parâmetros e acessar seus atributos:

```python
def duelo(guerreiro, mago):
    if guerreiro.energia > mago.mana:
        print(guerreiro.nome, "vence!")
    elif mago.mana > guerreiro.energia:
        print(mago.nome, "vence!")
    else:
        print("Empate.")
```

`duelo` não é método de nenhuma classe — fica solta no arquivo. Recebe dois objetos de tipos diferentes e compara atributos de cada um.

## 8. Organizando em arquivos

Num projeto maior, cada classe fica no seu próprio arquivo:

```
projeto/
├── personagem.py
└── main.py
```

**personagem.py**
```python
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def mostrar_status(self):
        print(self.nome, "-", self.vida, "de vida")
```

**main.py**
```python
from personagem import Personagem

thoric = Personagem("Thoric", 100, 15)
thoric.mostrar_status()
```

`from personagem import Personagem` — o nome antes do `import` é o nome do arquivo sem `.py`.

## Erros comuns

**Esquecer `self` no `def __init__`:**
```python
# errado
def __init__(nome, vida, ataque):

# certo
def __init__(self, nome, vida, ataque):
```
Python manda o objeto automaticamente como primeiro argumento. Se `self` não estiver lá, ele cai no lugar de `nome` e sobra um argumento.

**Esquecer de passar os valores na criação:**
```python
# errado — __init__ pede 3 valores
thoric = Personagem()

# certo
thoric = Personagem("Thoric", 100, 15)
```

**Usar `nome` em vez de `self.nome` dentro de outro método:**
```python
# errado
def mostrar_status(self):
    print(nome)  # NameError

# certo
def mostrar_status(self):
    print(self.nome)
```

`nome` só existiu como parâmetro dentro do `__init__`. Fora dele, o único acesso é via `self.nome`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `01_entendendo_init.pdf` | Leitura antes da aula — `__init__` em profundidade |
| `02_conceitos.py` | Exemplos comentados de classe, construtor e métodos |
| `03_exercicios.pdf` | Lista de exercícios da aula |
| `04_exercicios.py` | Arquivo pra resolver os exercícios |
| `Codigos/` | Pasta pra enviar o código resolvido |
