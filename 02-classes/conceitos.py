# ─────────────────────────────────────────────
#  CONCEITOS BÁSICOS DE POO
#  Execute este arquivo e leia o código junto
#  com o README para entender cada parte.
# ─────────────────────────────────────────────


# ═══════════════════════════════════════════
# 1. CLASSE SIMPLES — sem construtor
# ═══════════════════════════════════════════
# Uma classe é definida com a palavra "class".
# Por convenção, o nome começa com letra maiúscula.

class Lampada:
    acesa = False  # atributo de classe (compartilhado por todos os objetos)

    def ligar(self):
        self.acesa = True
        print("Lampada ligada.")

    def desligar(self):
        self.acesa = False
        print("Lampada desligada.")

    def verificar_estado(self):
        if self.acesa:
            print("A lampada esta LIGADA.")
        else:
            print("A lampada esta DESLIGADA.")


# Criando objetos e chamando métodos
l1 = Lampada()
l1.verificar_estado()   # A lampada esta DESLIGADA.
l1.ligar()              # Lampada ligada.
l1.verificar_estado()   # A lampada esta LIGADA.


print()
# ═══════════════════════════════════════════
# 2. CONSTRUTOR __init__
# ═══════════════════════════════════════════
# O construtor é chamado automaticamente quando
# o objeto é criado. Serve para definir os
# atributos iniciais de cada objeto.

class Aluno:
    def __init__(self, nome, nota):
        # self.nome e self.nota são atributos de instância
        # Cada objeto terá os seus próprios valores
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 7:
            print(f"{self.nome} esta Aprovado(a)!")
        else:
            print(f"{self.nome} esta Reprovado(a).")

    def apresentar_se(self):
        print(f"Ola, meu nome e {self.nome} e minha nota e {self.nota}.")


a1 = Aluno("Ana", 8.5)
a2 = Aluno("Bruno", 6.0)

a1.apresentar_se()          # Ola, meu nome e Ana e minha nota e 8.5.
a1.verificar_aprovacao()    # Ana esta Aprovado(a)!

a2.apresentar_se()          # Ola, meu nome e Bruno e minha nota e 6.0.
a2.verificar_aprovacao()    # Bruno esta Reprovado(a).


print()
# ═══════════════════════════════════════════
# 3. ACESSANDO E MODIFICANDO ATRIBUTOS
# ═══════════════════════════════════════════

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total_estoque(self):
        return self.preco * self.quantidade

    def exibir(self):
        total = self.valor_total_estoque()
        print(f"{self.nome} | R$ {self.preco:.2f} x {self.quantidade} unid. = R$ {total:.2f}")


p1 = Produto("Caderno", 12.50, 100)
p2 = Produto("Caneta", 2.99, 500)

p1.exibir()     # Caderno | R$ 12.50 x 100 unid. = R$ 1250.00
p2.exibir()     # Caneta | R$ 2.99 x 500 unid. = R$ 1495.00

# Modificar um atributo diretamente
p1.preco = 14.00
p1.exibir()     # Caderno | R$ 14.00 x 100 unid. = R$ 1400.00


print()
# ═══════════════════════════════════════════
# 4. MÚLTIPLOS OBJETOS — lista de objetos
# ═══════════════════════════════════════════

turma = [
    Aluno("Ana", 8.5),
    Aluno("Bruno", 6.0),
    Aluno("Carla", 9.2),
    Aluno("Diego", 5.5),
    Aluno("Elis", 7.0),
]

print("=== Resultado da turma ===")
soma = 0
for aluno in turma:
    soma += aluno.nota
    aluno.verificar_aprovacao()

media = soma / len(turma)
print(f"\nMedia da turma: {media:.2f}")


print()
# ═══════════════════════════════════════════
# 5. MÉTODOS QUE RETORNAM VALORES
# ═══════════════════════════════════════════
# Métodos podem usar "return" para devolver
# um resultado, igual a funções normais.

class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            print("Erro: divisao por zero.")
            return None
        return a / b


calc = Calculadora()
print(calc.somar(10, 5))       # 15
print(calc.subtrair(10, 5))    # 5
print(calc.multiplicar(10, 5)) # 50
print(calc.dividir(10, 5))     # 2.0
print(calc.dividir(10, 0))     # Erro: divisao por zero.
