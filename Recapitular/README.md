# Recapitulação de Python e Programação Orientada a Objetos

Esta pasta reúne o material de retomada usado antes da continuação do projeto de RPG.

Depois de uma pausa, é normal lembrar da ideia geral e esquecer detalhes de escrita, como a posição do `self`, a chamada de um método ou a condição de um `while`. A proposta desta recapitulação é reconstruir essas conexões em uma sequência curta, começando por uma classe simples e terminando em uma batalha funcional.

## Material principal

- [recap.pdf](recap.pdf): exercícios de aquecimento, retomada dos conceitos e continuação gradual do RPG.

O PDF foi preparado para uma aula de retomada. Os primeiros exercícios recuperam a estrutura de uma classe e os últimos conectam objetos, escolhas e repetição em um pequeno combate.

## Objetivos da retomada

Ao concluir o material, o estudante deverá conseguir:

- explicar a diferença entre classe e objeto;
- criar uma classe com `__init__`;
- usar `self` para acessar o estado do objeto;
- identificar atributos e métodos;
- criar objetos com valores diferentes;
- chamar métodos usando a notação de ponto;
- alterar atributos por meio de métodos;
- passar um objeto como argumento para outro objeto;
- organizar escolhas com `input()`, `if`, `elif` e `else`;
- controlar uma batalha com `while`;
- usar `random.randint()` para variar acontecimentos;
- explicar o fluxo completo de um turno;
- reconhecer onde a lógica pertence à classe e onde pertence ao programa principal.

## Conteúdos recuperados

### 1. Classe e objeto

Uma classe descreve quais dados e comportamentos um tipo de objeto terá. Um objeto é uma ocorrência concreta criada a partir dessa classe.

```python
class Personagem:
    pass


jogador = Personagem()
inimigo = Personagem()
```

`Personagem` é a classe. `jogador` e `inimigo` são objetos diferentes, mesmo que tenham sido criados a partir da mesma classe.

Uma classe funciona como uma definição. Ela informa como os objetos desse tipo serão organizados. Cada objeto mantém seu próprio estado durante a execução do programa.

### 2. Construtor `__init__`

O método `__init__` é executado quando um objeto é criado. Ele recebe os valores iniciais e os guarda nos atributos do objeto.

```python
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
```

Agora os objetos podem nascer com dados diferentes:

```python
jogador = Personagem("Thoric", 100, 15)
inimigo = Personagem("Goblin", 50, 8)
```

O construtor reduz a repetição e garante que todo personagem seja criado com os dados necessários.

### 3. O papel de `self`

`self` representa o objeto que está executando o método naquele momento.

Na criação abaixo:

```python
jogador = Personagem("Thoric", 100, 15)
```

durante a execução do `__init__`, `self` representa `jogador`.

Na criação seguinte:

```python
inimigo = Personagem("Goblin", 50, 8)
```

`self` passa a representar `inimigo` durante aquela nova execução.

Por isso, os dois objetos usam o mesmo código, mas mantêm valores independentes.

### 4. Atributos

Atributos guardam o estado de um objeto.

No RPG, alguns exemplos são:

- `nome`;
- `vida`;
- `ataque`;
- `defesa`;
- `pocoes`.

É possível consultar um atributo com a notação de ponto:

```python
print(jogador.nome)
print(jogador.vida)
```

Dentro da classe, os atributos são acessados por meio de `self`:

```python
print(self.nome)
print(self.vida)
```

### 5. Métodos

Métodos são funções definidas dentro de uma classe. Eles representam comportamentos dos objetos.

```python
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def mostrar_status(self):
        print(self.nome, "tem", self.vida, "pontos de vida.")
```

O método é chamado a partir de um objeto:

```python
jogador.mostrar_status()
inimigo.mostrar_status()
```

Python envia o próprio objeto automaticamente para o parâmetro `self`. Por isso, `self` aparece na definição do método, mas não aparece dentro dos parênteses na chamada.

### 6. Métodos que alteram o estado

Um método pode modificar os atributos do objeto.

```python
def receber_dano(self, quantidade):
    self.vida = self.vida - quantidade

    if self.vida < 0:
        self.vida = 0
```

Quando o método é chamado, a vida daquele objeto específico é alterada:

```python
inimigo.receber_dano(10)
```

Nesse caso, `self` representa `inimigo`. A vida do jogador não é modificada.

Impedir valores negativos também faz parte da responsabilidade do método. O objeto deve manter seu estado em uma condição válida.

### 7. Interação entre objetos

Um objeto pode receber outro objeto como argumento de um método.

```python
def atacar(self, alvo):
    alvo.receber_dano(self.ataque)
```

Na chamada:

```python
jogador.atacar(inimigo)
```

os papéis são:

- `self` representa o jogador;
- `alvo` representa o inimigo;
- `self.ataque` vem do jogador;
- `receber_dano()` é executado pelo inimigo;
- a vida alterada é a vida do inimigo.

Essa interação é uma das partes centrais do projeto. O jogador não altera diretamente a vida do inimigo. Ele solicita que o inimigo receba o dano por meio de um método.

### 8. Teste manual antes da automatização

Antes de construir o laço da batalha, cada método deve ser testado separadamente.

```python
jogador.atacar(inimigo)
inimigo.mostrar_status()

inimigo.atacar(jogador)
jogador.mostrar_status()
```

Esse teste confirma se:

- os objetos foram criados corretamente;
- o ataque usa o valor esperado;
- o alvo correto recebe o dano;
- a vida é atualizada;
- a vida não fica negativa;
- a exibição do estado está correta.

Quando os métodos funcionam isoladamente, fica mais fácil localizar problemas no laço principal.

### 9. Entrada de dados e escolhas

`input()` permite receber uma escolha digitada pelo jogador.

```python
escolha = input("Escolha uma ação: ")
```

O resultado de `input()` é texto. Se as opções forem comparadas com `"1"`, `"2"` e `"3"`, não é necessário converter.

```python
if escolha == "1":
    jogador.atacar(inimigo)
elif escolha == "2":
    jogador.defender()
elif escolha == "3":
    jogador.usar_pocao()
else:
    print("Opção inválida.")
```

Também é possível converter a entrada para número com `int()`, mas a comparação precisa ser consistente. Uma string `"1"` é diferente do número inteiro `1`.

### 10. Funções que organizam o programa

Nem toda lógica precisa ficar dentro de uma classe.

As classes descrevem os dados e comportamentos dos objetos. Uma função externa pode organizar uma etapa do jogo.

```python
def turno_do_jogador(jogador, inimigo):
    print("1 - Atacar")
    print("2 - Defender")
    print("3 - Usar poção")

    escolha = input("Escolha: ")

    if escolha == "1":
        jogador.atacar(inimigo)
    elif escolha == "2":
        jogador.defender()
    elif escolha == "3":
        jogador.usar_pocao()
    else:
        print("Opção inválida.")
```

A função decide quando uma ação acontece. O método da classe continua responsável por executar a ação.

Essa separação ajuda a evitar que a classe concentre o menu, a entrada do teclado, o laço e todas as regras do programa.

### 11. Laço principal da batalha

O `while` mantém a batalha em execução enquanto os dois personagens estiverem vivos.

```python
while jogador.vida > 0 and inimigo.vida > 0:
    jogador.mostrar_status()
    inimigo.mostrar_status()

    turno_do_jogador(jogador, inimigo)

    if inimigo.vida > 0:
        inimigo.atacar(jogador)
```

A condição possui duas partes:

- o jogador precisa estar vivo;
- o inimigo precisa estar vivo.

O operador `and` exige que as duas condições sejam verdadeiras.

Depois do turno do jogador, a vida do inimigo é verificada novamente. Essa verificação impede que um inimigo derrotado realize outro ataque.

### 12. Encerramento da batalha

Quando uma das vidas chega a zero, a condição do `while` deixa de ser verdadeira.

Depois do laço, o programa verifica quem continua vivo:

```python
if jogador.vida > 0:
    print("Você venceu!")
else:
    print("Você foi derrotado.")
```

O encerramento fica fora do `while` porque só deve acontecer uma vez, depois que a repetição terminar.

### 13. Aleatoriedade

O módulo `random` pode variar o dano, a chance de acerto ou a escolha do inimigo.

```python
import random
```

Um dano variável pode ser calculado assim:

```python
dano = random.randint(self.ataque - 3, self.ataque + 3)
```

Uma rolagem de vinte lados pode ser representada assim:

```python
rolagem = random.randint(1, 20)
```

O valor sorteado pode ser usado por uma decisão:

```python
if rolagem < 5:
    print(self.nome, "errou o ataque.")
else:
    alvo.receber_dano(self.ataque)
```

A aleatoriedade deve acrescentar variação, mas não substituir as regras. Primeiro é necessário definir o que cada faixa de resultado significa.

## Sequência recomendada de estudo

Para aproveitar melhor o PDF:

1. Responda às perguntas iniciais sem consultar o código anterior.
2. Complete a classe simples.
3. Execute o programa após cada pequena mudança.
4. Corrija os erros apresentados no material.
5. Implemente e teste `receber_dano()`.
6. Implemente e teste `atacar(alvo)`.
7. Faça uma batalha manual, sem `while`.
8. Organize a escolha do jogador.
9. Monte o laço completo.
10. Acrescente somente uma melhoria opcional por vez.

Não é necessário terminar todos os desafios para continuar o curso. A parte obrigatória termina quando uma batalha simples funciona do começo ao fim e o estudante consegue explicar o fluxo.

## Estratégia para encontrar erros

Quando o programa não funcionar, verifique uma parte por vez.

### O objeto foi criado?

Confira a quantidade e a ordem dos argumentos enviados ao construtor.

```python
jogador = Personagem("Thoric", 100, 15)
```

### O método tem `self`?

Todo método de instância precisa receber `self` como primeiro parâmetro.

```python
def mostrar_status(self):
    print(self.nome)
```

### O atributo usa `self`?

Dentro de um método, um atributo do objeto precisa ser acessado por `self`.

```python
self.vida = self.vida - quantidade
```

### O método foi chamado no objeto correto?

Leia a chamada da esquerda para a direita:

```python
jogador.atacar(inimigo)
```

O jogador executa `atacar`. O inimigo é recebido como alvo.

### O laço consegue terminar?

Algum valor usado na condição precisa mudar durante a repetição.

No RPG, a vida diminui quando os ataques acontecem. Quando uma vida chega a zero, o `while` termina.

### O inimigo derrotado ainda está atacando?

Verifique a vida do inimigo depois do turno do jogador e antes do turno do inimigo.

```python
if inimigo.vida > 0:
    inimigo.atacar(jogador)
```

### A entrada é texto ou número?

`input()` devolve uma string. Escolha uma forma de comparação e mantenha o mesmo tipo.

```python
escolha = input("Escolha: ")

if escolha == "1":
    jogador.atacar(inimigo)
```

## Perguntas para conferir a compreensão

Antes de avançar, tente responder sem executar o programa:

1. Qual é a diferença entre `Personagem` e `jogador`?
2. Quando o método `__init__` é executado?
3. O que `self` representa?
4. Por que `self.vida` pode ter um valor diferente em cada objeto?
5. Na chamada `jogador.atacar(inimigo)`, quem é `self`?
6. Na mesma chamada, quem é `alvo`?
7. Por que `receber_dano()` impede que a vida fique negativa?
8. Por que testar os ataques manualmente antes de criar o `while`?
9. Por que o inimigo precisa ter sua vida conferida antes de atacar?
10. O que faz o laço da batalha terminar?
11. Qual é a diferença entre mostrar um valor com `print()` e devolver um valor com `return`?
12. Qual lógica pertence aos métodos da classe?
13. Qual lógica pode ficar na função que organiza o turno?

## Critério de conclusão

A retomada está concluída quando o estudante consegue:

- criar dois personagens;
- mostrar o estado de cada personagem;
- fazer um personagem atacar o outro;
- explicar os papéis de `self` e `alvo`;
- escolher uma ação pelo teclado;
- repetir os turnos com `while`;
- impedir que um personagem derrotado continue atacando;
- exibir uma mensagem de vitória ou derrota;
- localizar um erro simples usando a mensagem do terminal e a sequência de execução.

O objetivo não é produzir um RPG completo nesta etapa. O objetivo é recuperar a base e deixar uma batalha pequena, compreensível e funcional. Essa estrutura será usada nas próximas aulas para organizar arquivos, criar tipos diferentes de personagem e ampliar o mundo do jogo.

## Como executar os códigos

Abra o terminal na pasta onde o arquivo Python foi salvo e execute:

```bash
python nome_do_arquivo.py
```

Em ambientes onde o comando principal é `python3`, use:

```bash
python3 nome_do_arquivo.py
```

Nenhuma biblioteca externa é necessária para os exercícios. O módulo `random` já faz parte da instalação padrão do Python.
