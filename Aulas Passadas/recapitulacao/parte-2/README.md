# Recapitulação de Python e POO: Dia 02

## Material da aula

- [Recapitulação de Python e POO, Parte 2](recapitulacao-python-poo-parte-2.pdf)

Esta pasta contém o material dos alunos para a segunda parte da recapitulação de Python e Programação Orientada a Objetos.

A proposta é retomar a escrita de código com exercícios práticos. O exemplo principal acompanha a construção de um RPG de terminal com personagens, ataques, defesa, poções, escolhas e batalhas.

O material não depende de códigos feitos antes da pausa. A apresentação parte de um arquivo vazio e fornece tudo o que será usado na aula. Os exercícios começam com variáveis, `print()`, `input()`, conversão, condições e `while`. A classe `Personagem` é criada somente depois desse aquecimento.

O tema do RPG mantém uma ligação com o restante do curso, mas nenhum arquivo dos Dias 1, 2, 3 ou 4 precisa estar pronto. Se o estudante não abriu o repositório durante a semana, ainda conseguirá acompanhar toda a retomada.

## Ponto de partida

Para acompanhar a apresentação, crie apenas um arquivo novo:

```bash
touch retomada.py
```

Também é possível criar o arquivo pelo editor e salvá-lo como `retomada.py`.

Não copie classes ou soluções anteriores. Cada bloco necessário aparece no PDF e será construído durante a aula.

O processo recomendado é:

1. Começar com o arquivo vazio.
2. Digitar somente o exemplo atual.
3. Prever a saída.
4. Executar.
5. Conferir os valores.
6. Corrigir antes de continuar.
7. Guardar somente as partes que serão usadas na etapa seguinte.

## Objetivo

Ao final da retomada, você deverá conseguir:

- Reconstruir a base de Python sem consultar um projeto anterior
- Usar variáveis, `print()`, `input()` e conversão de tipos
- Escrever decisões com `if`, `elif` e `else`
- Criar um `while` cuja condição consegue terminar
- Ler uma classe e encontrar seus atributos e métodos
- Criar objetos com estados diferentes
- Explicar o que `self` representa em uma chamada
- Alterar o estado de um objeto por meio de métodos
- Passar um objeto como argumento para outro objeto
- Testar métodos separadamente
- Usar `input()` para escolher uma ação
- Usar `random.randint()` para variar um resultado
- Criar um laço de batalha com `while`
- Impedir que um inimigo derrotado continue atacando
- Organizar vários inimigos em uma lista
- Encontrar erros comuns de escrita e lógica

## Como usar o PDF

Não leia o material apenas procurando respostas. Em cada exemplo, siga esta sequência:

1. Leia o código sem executar.
2. Identifique os objetos envolvidos.
3. Preveja qual atributo será alterado.
4. Anote o resultado esperado.
5. Execute o código.
6. Compare o resultado real com sua previsão.
7. Corrija uma parte por vez.
8. Explique o fluxo com suas próprias palavras.

O objetivo não é decorar o código. O objetivo é entender de onde os dados vêm, qual objeto executa o método e qual estado muda.

## Personagens usados

Os exemplos utilizam os seguintes personagens:

- Thoric, um guerreiro usado como jogador
- Elara, uma maga que pode ser usada como personagem alternativo
- Goblin, um inimigo inicial
- Orc, um inimigo com mais vida e defesa

Todos são criados a partir da classe `Personagem`. Cada objeto possui seu próprio estado.

## Estrutura principal

A classe evolui durante a apresentação até chegar a uma estrutura parecida com esta:

```python
class Personagem:
    def __init__(self, nome, vida, ataque, defesa, pocoes):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.pocoes = pocoes
        self.defendendo = False
```

Cada atributo possui uma função:

- `nome` identifica o personagem
- `vida` guarda a vida atual
- `vida_maxima` guarda o limite da cura
- `ataque` serve como base para o dano
- `defesa` reduz o dano recebido
- `pocoes` informa quantas curas ainda podem ser usadas
- `defendendo` informa se o próximo ataque deve ser reduzido

## Sequência da aula

### 1. Leitura da classe

O primeiro exercício pede que você encontre parâmetros, atributos, métodos, objetos e a saída esperada.

Leia cada linha e procure responder:

- Qual classe está sendo usada?
- Qual objeto foi criado?
- Quais valores foram enviados ao construtor?
- Qual método foi chamado?
- O método apenas mostra dados ou altera o objeto?

### 2. Previsão do estado

Antes de executar uma sequência de chamadas, anote a vida de cada personagem.

Exemplo:

```python
thoric.receber_dano(20)
goblin.receber_dano(12)
```

A primeira linha altera Thoric. A segunda linha altera Goblin.

O objeto que aparece antes do ponto é o objeto que executa o método.

### 3. Construtor completo

Complete os atributos usando `self`.

```python
self.nome = nome
self.vida = vida
```

O nome sem `self` é o parâmetro recebido. O nome com `self` é o atributo guardado no objeto.

### 4. Receber dano

O método `receber_dano()` precisa:

- receber a quantidade de ataque
- considerar a defesa
- impedir dano negativo
- reduzir a vida
- impedir que a vida fique abaixo de zero

Teste pelo menos três situações:

1. Ataque maior do que a defesa.
2. Ataque menor do que a defesa.
3. Ataque maior do que a vida restante.

### 5. Atacar outro objeto

Na chamada:

```python
thoric.atacar(goblin)
```

`self` representa Thoric e `alvo` representa Goblin.

O valor de ataque vem de Thoric. O método `receber_dano()` é executado pelo Goblin.

Leia a chamada da esquerda para a direita:

> Thoric executa atacar e recebe Goblin como alvo.

### 6. Defender

A defesa vale somente para o próximo ataque.

O método `defender()` muda `defendendo` para `True`. Depois que o personagem recebe o ataque reduzido, o atributo deve voltar para `False`.

Teste a sequência:

```python
thoric.defender()
thoric.receber_dano(20)
thoric.receber_dano(20)
```

O primeiro ataque deve ser reduzido. O segundo deve usar o cálculo normal.

### 7. Usar poção

A poção recupera vida e reduz a quantidade disponível.

O método deve tratar estas situações:

- ainda existem poções e falta vida
- não existem poções
- a vida já está cheia
- a cura ultrapassaria a vida máxima

A poção não deve ser descontada quando não puder ser usada.

### 8. Dano aleatório

O módulo `random` permite variar o resultado.

```python
import random

rolagem = random.randint(1, 20)
```

Os dois limites podem aparecer. Nesse exemplo, o resultado pode ser qualquer número inteiro entre 1 e 20.

O ataque deve verificar primeiro se acertou. O dano somente deve ser calculado e aplicado no caminho do acerto.

### 9. Escolha do jogador

`input()` sempre devolve texto.

```python
escolha = input("Escolha: ")

if escolha == "1":
    jogador.atacar(inimigo)
```

`"1"` é diferente de `1`. Se a entrada não foi convertida com `int()`, compare com texto.

A função de turno escolhe a ação. Os métodos da classe executam a ação.

### 10. Laço da batalha

A batalha deve continuar somente enquanto os dois personagens estiverem vivos.

```python
while jogador.vida > 0 and inimigo.vida > 0:
```

O operador correto é `and`. A batalha deve parar quando uma das duas vidas chegar a zero.

Depois do turno do jogador, confira novamente a vida do inimigo:

```python
if inimigo.vida > 0:
    inimigo.atacar(jogador)
```

Essa condição impede que um inimigo derrotado realize um contra-ataque.

### 11. Vários inimigos

Os inimigos podem ser guardados em uma lista:

```python
inimigos = [
    Personagem("Goblin", 40, 8, 2, 0),
    Personagem("Orc", 70, 12, 4, 0)
]
```

Um `for` externo escolhe o inimigo atual. Um `while` interno executa a batalha.

O jogador deve ser o mesmo objeto durante toda a sequência. Sua vida e suas poções não voltam aos valores iniciais entre as batalhas.

## Ordem recomendada para escrever o projeto

Crie o programa nesta ordem:

1. Classe e construtor.
2. Método `mostrar_status()`.
3. Método `receber_dano()`.
4. Três testes manuais de dano.
5. Método `atacar(alvo)`.
6. Teste manual entre dois objetos.
7. Método `defender()`.
8. Método `usar_pocao()`.
9. Dano aleatório e chance de acerto.
10. Função `turno_do_jogador()`.
11. Laço de uma batalha.
12. Lista com vários inimigos.

Não comece pelo `while`. Se os métodos ainda não funcionam, o laço apenas repetirá os erros.

## Estratégia de teste

Crie dois objetos:

```python
thoric = Personagem("Thoric", 100, 15, 5, 2)
goblin = Personagem("Goblin", 45, 8, 2, 0)
```

Mostre o estado inicial:

```python
thoric.mostrar_status()
goblin.mostrar_status()
```

Aplique dano direto:

```python
goblin.receber_dano(20)
goblin.mostrar_status()
```

Teste a interação:

```python
thoric.atacar(goblin)
goblin.mostrar_status()
```

Depois teste defesa e poção. Monte o laço somente quando cada método funcionar separadamente.

## Erros comuns

### Esquecer `self`

```python
# Incorreto
def atacar(alvo):
    pass

# Correto
def atacar(self, alvo):
    pass
```

### Usar o parâmetro fora do construtor

```python
# Incorreto
def mostrar_status(self):
    print(nome)

# Correto
def mostrar_status(self):
    print(self.nome)
```

### Comparar texto com número

```python
escolha = input("Escolha: ")

# Incorreto
if escolha == 1:
    pass

# Correto
if escolha == "1":
    pass
```

### Usar `or` na batalha

```python
# Incorreto
while jogador.vida > 0 or inimigo.vida > 0:
    pass

# Correto
while jogador.vida > 0 and inimigo.vida > 0:
    pass
```

### Permitir ataque depois da derrota

Confira a vida antes do contra-ataque:

```python
if inimigo.vida > 0:
    inimigo.atacar(jogador)
```

## Como investigar um problema

Faça estas perguntas:

1. O objeto foi criado com todos os argumentos?
2. O método possui `self`?
3. O atributo foi acessado com `self`?
4. O método foi chamado no objeto correto?
5. O alvo correto foi enviado?
6. A entrada é texto ou número?
7. Algum valor usado no `while` muda durante a repetição?
8. O inimigo está vivo antes do contra-ataque?
9. O estado mostrado no terminal corresponde ao objeto esperado?

Use `print()` temporariamente para observar valores importantes:

```python
print("Vida do jogador:", jogador.vida)
print("Vida do inimigo:", inimigo.vida)
print("Escolha recebida:", escolha)
```

Remova essas mensagens depois que o problema for resolvido.

## Desafios finais

### Ataque crítico

Use a rolagem de d20 para criar três resultados:

- 1 até 4: erro
- 5 até 18: dano normal
- 19 ou 20: dano dobrado

Mostre a rolagem e o dano no terminal.

### Inimigo curandeiro

Crie um Orc Xamã com uma poção. Em seu turno, ele deve escolher aleatoriamente entre atacar e tentar usar a poção.

O inimigo não pode:

- ultrapassar a vida máxima
- usar uma poção inexistente
- usar uma poção com a vida cheia
- agir depois de chegar a zero de vida

## Checklist final

- [ ] Criei a classe `Personagem` com todos os atributos
- [ ] Consigo explicar o que `self` representa
- [ ] Testei `receber_dano()` separadamente
- [ ] A vida nunca fica negativa
- [ ] A defesa vale somente para o próximo ataque
- [ ] A poção respeita a vida máxima
- [ ] A quantidade de poções diminui corretamente
- [ ] O ataque altera o alvo correto
- [ ] O ataque errado não causa dano
- [ ] O menu compara tipos compatíveis
- [ ] O `while` usa `and`
- [ ] O inimigo derrotado não contra-ataca
- [ ] O estado do jogador continua entre batalhas
- [ ] O programa termina com vitória ou derrota
- [ ] Consigo explicar o fluxo de um turno completo

## Como abrir o PDF

No Linux, usando Zathura:

```bash
zathura "Recapitular/dia-02/recapitulacao-python-poo-parte-2.pdf"
```

Também é possível abrir o arquivo pelo navegador ou pelo visualizador de documentos do sistema.
