# RPG Python

Esta pasta contém a base do projeto.

Use o PDF `rpg.pdf` durante a atividade.
O README segue os títulos das páginas do PDF.
Os títulos não usam o número da página.

O texto usa frases curtas.
Cada instrução contém uma ação principal.
Os mesmos termos têm o mesmo significado em todo o documento.

## O que está pronto

O arquivo `personagem.py` contém a classe `Personagem`.
O arquivo `main.py` contém o turno e o combate.
O jogo contém três inimigos.

Esta base representa o trabalho anterior da turma.
Não altere todos os arquivos de uma vez.
Execute a base antes de iniciar uma atividade.

## O que você vai construir

Você vai ampliar o RPG.
Você vai criar um inventário.
Você vai criar itens com efeitos diferentes.
Você vai conectar os itens ao personagem.
Você vai usar a mesma operação para itens diferentes.

A pasta não contém a solução dessas partes.
As seções deste README contêm perguntas, passos e verificações.

## Prepare a pasta no VS Code

### Se você recebeu esta pasta pronta

- Abra o VS Code.
- Selecione **File > Open Folder**.
- Selecione a pasta `RPG Python/dia-05`.
- Selecione **Open**.
- Confirme que `main.py` e `personagem.py` aparecem no Explorer.

### Se você precisa criar uma pasta nova

- Abra o VS Code.
- Selecione **File > Open Folder**.
- Selecione **New Folder**.
- Crie primeiro a pasta `RPG Python`.
- Dentro dela, crie a pasta `dia-05`.
- Abra a nova pasta.
- Use o botão **New File** no Explorer.
- Crie `main.py`.
- Crie `personagem.py`.

Não use espaços no nome dos arquivos.
Use letras minúsculas nos nomes dos módulos Python.

### Abra o terminal do VS Code

- Selecione **Terminal > New Terminal**.
- Confirme que o terminal mostra a pasta `dia-05`.
- Execute um dos comandos abaixo.

No Linux ou no macOS:

```bash
python3 --version
python3 main.py
```

No Windows:

```powershell
python --version
python main.py
```

Se o comando não funcionar, confirme a instalação do Python.
Não instale bibliotecas para este projeto.
O projeto usa somente recursos do Python.

### Crie um ambiente virtual opcional

Esta etapa é opcional.
Use esta etapa para manter o ambiente do projeto separado.

No Linux ou no macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Depois da ativação, execute `main.py` novamente.

## Como usar este guia

- Abra o PDF.
- Encontre o mesmo título neste README.
- Leia a seção completa.
- Faça uma ação por vez.
- Execute o programa depois de uma mudança pequena.
- Compare o resultado com sua previsão.
- Corrija um problema por vez.

Não copie uma solução pronta.
Use as perguntas para localizar a regra correta.

---

## RPG Python: lembrar, explicar e avançar

O projeto não começa do zero.
Você já tem uma classe e um combate.

Antes de escrever código novo, execute a base.
Use uma opção de cada vez.
Observe a vida dos dois objetos.

Ao final desta etapa, você deve conseguir fazer estas ações:

- localizar a classe `Personagem`;
- localizar a criação dos objetos;
- localizar o laço do combate;
- localizar a linha que altera a vida;
- explicar o próximo objetivo do projeto.

## A trajetória até aqui

Antes da pausa, você estudou classes e objetos.
Você também estudou `__init__`, `self`, atributos e métodos.

Depois da pausa, você revisou a teoria.
Depois, você escreveu código do RPG.

Agora você vai conectar essas partes.
Não tente memorizar cada linha.
Identifique o objeto, a ação e a mudança de estado.

## Vocês já construíram estas peças

Abra `personagem.py`.
Localize a classe `Personagem`.
Localize os atributos do construtor.
Localize os métodos de combate.

Abra `main.py`.
Localize o jogador.
Localize a lista de inimigos.
Localize o turno.
Localize o combate.

Use esta pergunta em toda chamada de método:

> Qual objeto executa a ação e qual objeto muda?

## O mapa do projeto

O arquivo `personagem.py` guarda as regras do personagem.
O arquivo `main.py` organiza o fluxo do jogo.

Não mova `input()` para a classe `Personagem`.
Não calcule o dano dentro do menu.

Use esta regra:

- O objeto protege seu estado.
- O programa principal organiza a sequência.

## Classe é o molde; objeto é um estado real

A classe descreve os dados e as ações possíveis.
Um objeto contém valores reais.

Localize `jogador` e o primeiro inimigo.
Compare os valores de vida.
Compare os valores de ataque.

Faça uma previsão:

- Se o Goblin perde vida, a vida de Thoric também muda?
- Se Thoric usa uma poção, a quantidade de poções do Orc muda?

Execute o programa para confirmar sua resposta.

## __init__ prepara o estado inicial

O método `__init__` prepara um objeto novo.
Cada parâmetro fornece um valor inicial.

Localize estes atributos:

- `nome`;
- `vida`;
- `vida_maxima`;
- `ataque`;
- `defesa`;
- `pocoes`;
- `defendendo`.

Separe os atributos em três grupos:

- valor que não muda durante o combate;
- valor que pode mudar;
- valor que representa uma condição temporária.

## self é o objeto que recebeu a chamada

Leia uma chamada da esquerda para a direita.
O objeto antes do ponto recebe a chamada.

Na chamada `jogador.atacar(inimigo)`, `self` representa `jogador`.
O parâmetro `alvo` representa `inimigo`.

Faça o mesmo processo com estas chamadas:

- `jogador.defender()`;
- `inimigo.atacar(jogador)`;
- `jogador.usar_pocao()`.

Não responda somente “self é ele mesmo”.
Diga o nome do objeto.

## Métodos alteram estado com regras

O método `receber_dano()` altera a vida.
Ele também protege limites.

Leia o método de cima para baixo.
Anote o valor de cada variável.

Confirme estas regras:

- a defesa reduz o dano;
- o dano não fica negativo;
- a vida não fica negativa;
- a defesa temporária volta para `False`.

## Objetos podem colaborar

O método `atacar()` calcula um dano.
Depois, ele chama um método do alvo.

O atacante não altera a vida do alvo diretamente.
O alvo aplica sua própria regra de dano.

Siga este caminho:

- localize a chamada de `atacar()`;
- identifique `self`;
- identifique `alvo`;
- localize a chamada de `receber_dano()`;
- localize a mudança de `vida`.

## Onde cada responsabilidade deve ficar?

Use uma responsabilidade principal para cada parte.

`Personagem` deve cuidar destas regras:

- receber dano;
- atacar;
- defender;
- usar uma poção;
- informar se está vivo.

`main.py` deve cuidar destas regras:

- mostrar o menu;
- receber a escolha;
- repetir o combate;
- escolher o próximo inimigo;
- encerrar o jogo.

## Acompanhe um ataque completo

Use papel ou um comentário temporário.
Anote o estado antes do ataque.

Registre estes valores:

- vida do atacante;
- vida do alvo;
- ataque do atacante;
- defesa do alvo;
- estado `defendendo` do alvo.

Execute um ataque.
Registre os mesmos valores novamente.
Explique somente os valores que mudaram.

## Defesa é um estado temporário

O método `defender()` muda `defendendo` para `True`.
O próximo dano usa esse valor.
Depois, o método restaura `False`.

Teste esta sequência:

- mostre o estado inicial;
- prepare a defesa;
- receba um dano;
- mostre o estado;
- receba outro dano;
- compare os dois resultados.

Não mantenha a defesa ativa para sempre.

## A poção precisa respeitar limites

O método `usar_pocao()` verifica o estado antes da cura.

Teste estes casos separadamente:

- personagem sem poções;
- personagem com vida cheia;
- personagem com pouca vida;
- cura maior que o espaço disponível.

Depois de cada caso, confirme `vida` e `pocoes`.

## O turno traduz uma escolha em ação

O turno recebe um texto.
Por isso, o código compara a escolha com `"1"`, `"2"` e `"3"`.

O turno seleciona uma ação.
O método do personagem executa a regra.

Teste também uma opção inválida.
Confirme que o programa não encerra por causa dessa entrada.

## combate() controla repetição e encerramento

O laço depende da vida dos dois objetos.
O inimigo age somente se estiver vivo.

Localize estas decisões:

- condição do `while`;
- chamada do turno do jogador;
- verificação antes do ataque inimigo;
- retorno de vitória;
- retorno de derrota.

Explique por que a função retorna um valor booleano.

## Um jogador enfrenta vários objetos

O laço `for` seleciona um inimigo por vez.
O jogador não é criado novamente.

Observe o estado do jogador entre duas batalhas.
Confirme que a vida continua com o valor atual.
Confirme que as poções continuam com a quantidade atual.

O comando `break` encerra a sequência após uma derrota.

## A herança que vocês já experimentaram

Herança representa uma relação “é um”.

Use estes exemplos como referência:

- Guerreiro é um Personagem;
- Mago é um Personagem;
- Inimigo é um Personagem.

Uma subclasse deve acrescentar uma diferença real.
Não crie uma subclasse somente para trocar o nome.

Esta base inicial não fornece essas subclasses.
Use seus exercícios anteriores para revisar esse assunto.

## A composição que vocês já tocaram

Composição representa uma relação “tem um”.

O novo objetivo usa estas relações:

- Personagem tem um inventário;
- Inventário tem itens;
- Item tem um efeito.

Não escreva a solução ainda.
Primeiro, diga qual objeto deve guardar cada informação.

## Antes de avançar, consigam explicar

> **EXERCÍCIO**

Responda sem alterar o código.

- Quem é `self` durante um ataque do jogador?
- Qual objeto perde vida?
- Onde a defesa volta para `False`?
- Por que a vida não fica negativa?
- Por que `input()` fica em `main.py`?
- Por que um inimigo morto não ataca?
- Por que o jogador não é criado novamente?
- Qual é a diferença entre “é um” e “tem um”?

Mostre a linha que confirma cada resposta.

## Um ciclo para resolver cada desafio

Use sempre a mesma sequência.

- Leia a regra.
- Identifique os objetos.
- Anote o estado inicial.
- Faça uma previsão.
- Execute o programa.
- Compare o resultado.
- Faça uma mudança pequena.
- Execute novamente.
- Explique a mudança.

Não faça várias mudanças antes do teste.

## Como receber_dano() organiza as regras

Leia `receber_dano()` sem editar o arquivo.

Identifique a ordem das operações:

- receber a quantidade;
- subtrair a defesa;
- aplicar a defesa temporária;
- impedir dano negativo;
- alterar a vida;
- impedir vida negativa.

Trocar a ordem pode trocar o resultado.
Explique por que a ordem atual faz sentido.

## Agora prevejam sem executar

> **EXERCÍCIO**

Use o primeiro caso do PDF.
Anote o dano real.
Anote a vida final.
Anote o valor final de `defendendo`.

Depois, use o segundo caso.
Mostre cada operação.

Não execute o código antes de concluir as duas previsões.

## Executem e comparem com a previsão

> **EXERCÍCIO**

Crie um arquivo temporário chamado `teste_manual.py`.
Use esse arquivo somente para testar a classe.

Faça estas ações:

- importe `Personagem`;
- crie um objeto com os valores do PDF;
- mostre o estado inicial;
- execute o primeiro dano;
- prepare a defesa;
- execute o segundo dano;
- mostre o estado final.

Compare o resultado com sua previsão.
Apague somente os testes que não serão mais úteis.

## Mudem uma regra pequena

> **EXERCÍCIO**

Faça uma cópia de `personagem.py` antes da mudança.
Use o nome `personagem_original.py`.

Altere somente a redução da defesa temporária.
Use a regra indicada no PDF.

Depois, execute os testes anteriores.
Confirme estas condições:

- a defesa ainda termina após um ataque;
- o dano não fica negativo;
- a vida não fica negativa;
- o caso sem defesa continua correto.

## Explique o caminho do estado

> **EXERCÍCIO**

Escolha um dos testes.
Explique o teste de cima para baixo.

Use estes termos:

- objeto;
- estado inicial;
- parâmetro;
- regra;
- estado final.

Mostre a linha que altera `vida`.
Mostre a linha que altera `defendendo`.

## Quando falhar, sigam o estado

> **EXERCÍCIO**

Não altere o programa imediatamente.
Primeiro, identifique o sintoma.

Adicione saídas temporárias antes e depois da operação suspeita.
Mostre somente os valores relacionados ao problema.

Use esta ordem:

- reproduza o erro;
- mostre o estado inicial;
- execute uma ação;
- mostre o estado final;
- localize a primeira diferença;
- altere uma linha;
- execute novamente.

## O RPG está crescendo

Os novos itens criam novas responsabilidades.
Não coloque todos os efeitos dentro de `Personagem`.

Liste os dados de um item.
Liste as ações de um item.
Liste as regras do inventário.

Mantenha as regras de vida e dano em `Personagem`.

## Antes de criar uma classe, faça três perguntas

Para cada classe nova, responda:

- Qual informação esta classe guarda?
- Qual regra esta classe protege?
- Com qual objeto esta classe colabora?

Se duas classes tiverem a mesma responsabilidade, revise a divisão.
Se uma classe não tiver responsabilidade, não crie essa classe.

## Personagem tem um inventário

Crie a relação por composição.
Não transforme `Inventario` em uma subclasse de `Personagem`.

O personagem deve guardar uma referência para o inventário.
O inventário deve guardar os itens.

Use métodos para conectar os objetos.
Não acesse a lista em muitos lugares diferentes.

## Item guarda dados e oferece um comportamento

Crie o arquivo `item.py` quando o PDF solicitar.

Defina primeiro a responsabilidade do item.
Use os nomes de atributos indicados no PDF.

Não implemente todos os efeitos na classe base.
Prepare uma operação comum para uso futuro.

Faça estas perguntas:

- Quem usa o item?
- Quem recebe o efeito?
- Qual estado pode mudar?
- Qual método deve proteger essa mudança?

## Inventario protege a coleção

Crie o arquivo `inventario.py`.

O inventário deve controlar a coleção.
O personagem não deve alterar a lista diretamente.

Comece com estas capacidades:

- adicionar um item;
- listar os itens;
- localizar um item escolhido;
- remover um item consumido.

Implemente uma capacidade por vez.
Teste cada capacidade antes de continuar.

## Conecte os objetos primeiro

> **EXERCÍCIO**

Faça esta atividade antes de criar efeitos.

- Crie `item.py`.
- Crie `inventario.py`.
- Crie um inventário para o personagem.
- Crie uma operação para pegar um item.
- Crie um item simples.
- Adicione o item ao inventário.
- Liste o conteúdo.

O item deve aparecer uma vez.
O personagem deve continuar funcionando no combate.

## Agora crie dois comportamentos

> **EXERCÍCIO**

Crie um item de cura.
Crie um item de ataque.

O item de cura deve respeitar `vida_maxima`.
O item de ataque deve usar `receber_dano()`.

Não altere `vida` do alvo diretamente no item de ataque.
Não deixe a cura ultrapassar o limite.

Teste cada item separadamente.
Depois, teste os dois itens no mesmo inventário.

## A mesma mensagem, comportamentos diferentes

Os dois itens devem aceitar a mesma operação de uso.
Cada item deve executar seu próprio efeito.

O programa principal não deve calcular a cura.
O programa principal não deve calcular o dano do item.

Verifique o fluxo:

- o jogador escolhe um item;
- o jogo solicita o uso;
- o item executa o efeito;
- o objeto afetado protege seu estado.

Este padrão prepara o conceito de polimorfismo.

## O caminho das próximas aulas

Primeiro, conclua a composição.
Depois, aplique o mesmo método a itens diferentes.

As próximas etapas podem incluir:

- capacidade máxima do inventário;
- equipamento que altera atributos;
- efeitos com duração;
- ações polimórficas;
- encapsulamento de atributos;
- testes automatizados;
- persistência do jogo.

Adicione uma etapa somente quando a base estiver estável.

## Mostrem, expliquem e escolham o próximo passo

> **EXERCÍCIO**

Execute uma demonstração final.

Mostre estas partes:

- um personagem em combate;
- um inventário com dois itens;
- o uso do item de cura;
- o uso do item de ataque;
- um caso limite;
- o estado antes e depois de cada item.

Explique estas decisões:

- por que o personagem tem um inventário;
- por que o inventário controla a coleção;
- por que o item de ataque usa `receber_dano()`;
- por que os itens usam a mesma operação;
- qual parte deve ser melhorada depois.

## Critérios de conclusão

O projeto está concluído quando todas as condições abaixo forem verdadeiras.

- A base de combate ainda funciona.
- O jogador possui um inventário.
- O inventário lista os itens.
- O item de cura respeita a vida máxima.
- O item de ataque usa a regra de dano existente.
- Um item consumido pode sair do inventário.
- Itens diferentes usam a mesma operação principal.
- O código não contém uma solução diferente para cada item em `main.py`.
- Você consegue explicar quais objetos mudam em cada ação.
