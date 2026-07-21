# Recapitulação de Python e Programação Orientada a Objetos

Esta pasta reúne o material de retomada usado antes da continuação do projeto de RPG.

Depois de uma pausa, é normal lembrar da ideia geral e esquecer detalhes de escrita, como a posição do `self`, a chamada de um método ou a condição de um `while`. A proposta desta recapitulação é reconstruir essas conexões em uma sequência curta, começando por uma classe simples e terminando em uma batalha funcional.

## Materiais disponíveis

### Parte 1

- [recap.pdf](recap.pdf): retomada teórica e exercícios iniciais sobre Python, classes, objetos, métodos, entrada de dados, condições e repetição.

Esse material recupera os conceitos necessários para acompanhar o projeto. Ele pode ser usado como leitura anterior, consulta durante a aula ou revisão individual.

### Parte 2

- [recapitulacao-python-poo-parte-2.pdf](dia-02/recapitulacao-python-poo-parte-2.pdf): apresentação dos alunos, com leitura de código, previsão de estado, implementação, testes, depuração e integração do RPG.

A apresentação da Parte 2 foi preparada para uma aula guiada de 60 a 90 minutos. O conteúdo começa com uma classe pequena e avança até uma batalha por turnos com vários inimigos. Os exemplos principais seguem o mesmo tema e a mesma progressão dos Dias 3 e 4 deste repositório.

## Como escolher o material

Use a Parte 1 quando a turma ainda precisa recuperar definições, reconhecer a estrutura de uma classe ou relembrar a diferença entre atributo e método.

Use a Parte 2 quando a turma já reconhece os conceitos, mas ainda precisa praticar a leitura e a escrita do código. Ela foi pensada para estudantes que entendem a ideia geral e ainda cometem erros de indentação, uso de `self`, comparação entre texto e número, chamada de métodos, condição do `while` e alteração do estado dos objetos.

Uma sequência possível é:

1. Usar a Parte 1 como leitura ou revisão curta.
2. Abrir a Parte 2 em sala.
3. Pedir previsões antes de executar os exemplos.
4. Escrever cada método com a turma.
5. Testar o método antes de montar o laço completo.
6. Encerrar com um dos desafios propostos.

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

## Guia da apresentação da Parte 2

Esta seção ajuda a preparar e conduzir a apresentação `dia-02/recapitulacao-python-poo-parte-2.pdf`. A organização acompanha a ordem das páginas do arquivo.

### Página 1: abertura

A primeira página apresenta o objetivo da retomada: transformar métodos testados separadamente em um RPG funcional no terminal.

Não é necessário explicar novamente toda a definição de POO. O ponto principal é mostrar que a turma já conhece as peças e agora precisa conectá-las.

Uma boa pergunta para iniciar é:

> O que falta para uma classe com métodos de ataque virar um jogo completo?

A resposta deve mencionar a organização dos turnos, a entrada do jogador e o laço da batalha.

### Página 2: processo de trabalho

A sequência usada durante toda a aula é:

1. Ler o código.
2. Prever o resultado.
3. Escrever ou completar uma parte.
4. Executar.
5. Encontrar e corrigir erros.
6. Integrar a parte ao programa.

Essa ordem reduz a quantidade de problemas acontecendo ao mesmo tempo. Um método pequeno é mais fácil de testar do que um jogo inteiro.

Peça aos alunos que evitem copiar todas as páginas antes de executar. Cada bloco deve ser testado assim que estiver completo.

### Página 3: leitura da classe

A classe `Personagem` aparece com os atributos básicos `nome`, `vida` e `ataque`.

Antes de mostrar a resposta, peça que a turma encontre:

- os parâmetros do construtor;
- os atributos criados;
- o método que apenas consulta o estado;
- o objeto criado;
- a saída esperada.

O exercício não pede uma definição decorada. Ele pede que o estudante encontre cada parte dentro de um código real.

### Página 4: previsão do estado

Thoric e Goblin são objetos diferentes. Cada chamada de `receber_dano()` altera somente o objeto que aparece antes do ponto.

Leia uma linha por vez e registre os valores de vida antes de avançar. A última chamada causa um dano maior do que a vida disponível. O método deve impedir que a vida fique negativa.

Esse exercício prepara a turma para acompanhar alterações de estado dentro do combate.

### Página 5: construtor completo

O construtor passa a receber:

- `nome`;
- `vida`;
- `ataque`;
- `defesa`;
- `pocoes`.

Também são criados `vida_maxima` e `defendendo`.

`vida_maxima` guarda o limite usado pela poção. O valor inicial é igual à vida inicial porque o personagem começa com a vida cheia.

`defendendo` começa com `False` porque o personagem ainda não escolheu a ação de defesa.

### Página 6: receber dano

O método `receber_dano()` protege o estado do personagem.

O cálculo segue esta ordem:

1. Receber a quantidade de ataque.
2. Subtrair a defesa.
3. Impedir dano negativo.
4. Reduzir a vida.
5. Impedir vida negativa.

Os três testes manuais representam situações diferentes:

- dano maior do que a defesa;
- ataque menor do que a defesa;
- dano maior do que toda a vida restante.

Peça que os alunos confiram o atributo `vida` depois de cada chamada. Não avance para `atacar()` enquanto esses testes não produzirem o resultado esperado.

### Página 7: interação entre objetos

Na chamada abaixo:

```python
thoric.atacar(goblin)
```

os papéis são:

- `self` representa `thoric`;
- `alvo` representa `goblin`;
- o ataque vem de `thoric.ataque`;
- `receber_dano()` é executado por `goblin`;
- a vida alterada pertence ao Goblin.

Uma forma simples de ler a chamada é:

> Thoric executa atacar e recebe Goblin como alvo.

Essa leitura ajuda a evitar a troca entre atacante e alvo.

### Página 8: defesa temporária

O método `defender()` não reduz a vida imediatamente. Ele muda o atributo `defendendo` para `True`.

O próximo ataque consulta esse estado, reduz o dano pela metade e volta `defendendo` para `False`.

O reset é parte importante da regra. Sem ele, todos os ataques seguintes seriam reduzidos.

Teste a sequência completa:

```python
thoric.defender()
thoric.receber_dano(20)
thoric.receber_dano(20)
```

O primeiro dano deve ser reduzido. O segundo deve voltar ao cálculo normal.

### Página 9: uso de poção

O método `usar_pocao()` possui três caminhos principais:

1. Não existem poções.
2. A vida já está cheia.
3. A poção pode ser usada.

A quantidade de poções deve diminuir somente no terceiro caminho.

Se a cura ultrapassar `vida_maxima`, a vida deve ser ajustada ao limite. Por exemplo, um personagem com 90 de vida e limite 100 não pode terminar com 115.

Os casos de borda são tão importantes quanto o uso normal. Eles mostram se o método mantém o objeto em um estado válido.

### Página 10: aleatoriedade

O ataque passa a ter duas etapas:

1. Rolar a chance de acerto com `random.randint(1, 20)`.
2. Calcular o dano variável somente quando o ataque acertar.

Os dois limites de `randint()` podem aparecer. Uma rolagem de 1 até 20 pode gerar tanto 1 quanto 20.

No exemplo da apresentação, valores menores que 5 representam erro. Nesse caminho, `receber_dano()` não pode ser chamado.

Depois de um acerto, o dano varia entre `self.ataque - 3` e `self.ataque + 3`.

### Página 11: menu de ações

A função `turno_do_jogador()` organiza a escolha, mas não repete as regras dos métodos.

Cada opção chama algo que já foi testado:

- opção `"1"`: `jogador.atacar(inimigo)`;
- opção `"2"`: `jogador.defender()`;
- opção `"3"`: `jogador.usar_pocao()`.

`input()` devolve texto. Por isso, a comparação usa `"1"`, `"2"` e `"3"`.

Também seria possível converter a entrada com `int()`, mas nesse caso todas as comparações precisariam usar números. A regra principal é manter os tipos consistentes.

### Página 12: laço da batalha

A condição correta exige que os dois personagens estejam vivos:

```python
while jogador.vida > 0 and inimigo.vida > 0:
```

O operador `and` é necessário porque a batalha deve parar assim que uma das vidas chegar a zero.

A ordem do turno é:

1. Conferir as vidas na condição do `while`.
2. Mostrar o estado atual.
3. Executar o turno do jogador.
4. Conferir novamente a vida do inimigo.
5. Permitir o contra-ataque somente se o inimigo estiver vivo.

A verificação do passo 4 impede que um inimigo derrotado ataque uma última vez.

### Página 13: depuração

Os cinco erros apresentados são frequentes neste conteúdo:

1. Método sem `self`.
2. Uso de `nome` em vez de `self.nome`.
3. Comparação de `"1"` com `1`.
4. Uso de `or` onde a batalha precisa de `and`.
5. Contra-ataque sem verificar a vida do inimigo.

Antes de mostrar as correções, dê um tempo para a turma apontar o sintoma de cada erro.

É importante separar erro de sintaxe, erro de execução e erro de lógica. Um programa pode executar sem mensagem vermelha e ainda produzir um resultado errado.

### Página 14: vários inimigos

A lista guarda os inimigos que serão enfrentados:

```python
inimigos = [
    Personagem("Goblin", 40, 8, 2, 0),
    Personagem("Orc", 70, 12, 4, 0)
]
```

O `for` externo escolhe um inimigo por vez. O `while` interno executa a batalha contra o inimigo atual.

O jogador não é criado novamente dentro do `for`. Por isso, sua vida e suas poções continuam com os valores deixados pela batalha anterior.

Se o jogador chegar a zero de vida, `break` interrompe a sequência.

### Página 15: mapa do programa

Essa página mostra a responsabilidade de cada parte:

- a classe guarda estado e métodos;
- os objetos representam jogador e inimigos;
- `turno_do_jogador()` lê a escolha;
- os métodos executam as ações;
- o laço de combate organiza a repetição;
- o programa principal cria e conecta tudo.

Use o mapa para perguntar onde uma nova regra deveria ser colocada. Uma regra de dano pertence à classe. Uma escolha digitada pertence à função de turno. A criação dos objetos pertence ao programa principal.

### Página 16: desafios

O primeiro desafio amplia a rolagem de d20:

- 1 até 4 representa erro;
- 5 até 18 representa dano normal;
- 19 ou 20 representa dano crítico.

O segundo desafio cria um Orc Xamã que pode atacar ou usar uma poção. Ele precisa respeitar as mesmas regras de vida máxima, quantidade de poções e encerramento do turno.

Os desafios devem ser implementados em pequenas partes. Primeiro teste a nova regra isolada. Depois integre ao combate.

### Página 17: consulta rápida

A última página resume a escrita necessária para continuar praticando:

- `__init__`;
- uso de `self`;
- passagem do alvo;
- comparação de entrada;
- `random.randint()`;
- condição do combate;
- sequência de depuração.

Ela pode ficar projetada durante a atividade final ou ser consultada depois da aula.

## Sugestão de roteiro para 60 minutos

- 5 minutos para abertura e processo de trabalho.
- 10 minutos para leitura, previsão de estado e construtor.
- 15 minutos para dano, ataque, defesa e poção.
- 10 minutos para aleatoriedade e menu.
- 10 minutos para laço completo e depuração.
- 5 minutos para vários inimigos e mapa do programa.
- 5 minutos para apresentar o desafio e a folha de consulta.

## Sugestão de roteiro para 90 minutos

- 10 minutos para abertura, leitura e previsão.
- 15 minutos para completar o construtor e implementar dano.
- 15 minutos para ataque, defesa e poção.
- 15 minutos para aleatoriedade e menu.
- 15 minutos para laço completo e correção dos erros.
- 10 minutos para vários inimigos.
- 10 minutos para iniciar um desafio em dupla.

## Como conduzir a escrita ao vivo

Digite o código em blocos pequenos. Depois de cada bloco, faça uma pergunta que possa ser respondida observando o estado.

Exemplos:

- Qual objeto terá a vida alterada?
- Qual valor está em `self` nesta chamada?
- A poção deve ser descontada neste caminho?
- A condição do laço ainda é verdadeira?
- O inimigo pode agir depois desta linha?

Evite entregar o programa completo logo no início. Quando todas as partes aparecem ao mesmo tempo, os alunos podem encontrar um erro no `while` e acreditar que o problema está no método de ataque.

## Estratégia de teste recomendada

Comece criando dois objetos:

```python
thoric = Personagem("Thoric", 100, 15, 5, 2)
goblin = Personagem("Goblin", 45, 8, 2, 0)
```

Teste a leitura do estado:

```python
thoric.mostrar_status()
goblin.mostrar_status()
```

Teste dano direto:

```python
goblin.receber_dano(20)
goblin.mostrar_status()
```

Teste interação:

```python
thoric.atacar(goblin)
goblin.mostrar_status()
```

Teste defesa e poção. Somente depois desses testes, crie `turno_do_jogador()` e o `while`.

## Lista de verificação para o professor

Antes da aula:

- [ ] Abrir o PDF dos alunos.
- [ ] Confirmar que Python está disponível nos computadores.
- [ ] Preparar um arquivo vazio para a codificação ao vivo.
- [ ] Confirmar que o módulo `random` funciona.

Durante a aula:

- [ ] Pedir uma previsão antes de executar.
- [ ] Conferir a indentação com a turma.
- [ ] Mostrar o estado dos objetos depois das chamadas.
- [ ] Testar casos normais e casos de borda.
- [ ] Explicar a diferença entre regra da classe e organização do programa.
- [ ] Conferir a vida do inimigo antes do contra-ataque.

Depois da aula:

- [ ] Verificar se cada estudante consegue criar dois personagens.
- [ ] Verificar se o ataque altera o alvo correto.
- [ ] Verificar se a batalha termina.
- [ ] Verificar se o estudante explica um erro encontrado.
- [ ] Registrar quais partes precisam de nova prática.

## Perguntas de apoio durante a prática

Quando um aluno estiver travado, faça perguntas curtas antes de indicar a resposta:

- Qual objeto aparece antes do ponto?
- Qual método está sendo chamado?
- Quais argumentos foram enviados?
- Qual atributo deveria mudar?
- O atributo mudou no objeto correto?
- O valor recebido por `input()` é texto ou número?
- Algum valor da condição do `while` muda dentro do laço?
- O caminho do erro ainda chama `receber_dano()`?
- O inimigo ainda está vivo antes do contra-ataque?

Essas perguntas ajudam o estudante a reconstruir o fluxo sem depender de uma solução pronta.

## Resultado esperado

Ao final, o estudante deve conseguir explicar uma execução parecida com esta:

1. O programa cria o jogador e o inimigo.
2. O `while` confirma que ambos estão vivos.
3. A função de turno recebe a escolha.
4. A escolha chama um método do jogador.
5. O método pode alterar o estado do alvo ou do próprio jogador.
6. O programa confere se o inimigo sobreviveu.
7. O inimigo contra-ataca somente se estiver vivo.
8. A repetição continua enquanto as duas vidas forem maiores que zero.
9. O programa mostra vitória ou derrota quando o laço termina.

O estudante não precisa decorar cada linha. Ele precisa entender a ordem, reconhecer os objetos envolvidos e localizar a parte responsável por cada mudança.

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
