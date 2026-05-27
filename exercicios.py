# ============================================================
#  exercicios.py — Funções de cada exercício de lógica
#  Projeto: py-logic-lab | Rocketseat Style
# ============================================================


def somar_dois_numeros():
    """Exercício 1 — Entrada de dados + operador matemático"""
    print("\n  📌 Exercício 1: Somar dois números")
    print("  " + "-" * 38)

    try:
        a = float(input("  Digite o primeiro número: "))
        b = float(input("  Digite o segundo número:  "))
        resultado = a + b
        print(f"\n  ✅ {a} + {b} = {resultado}")
    except ValueError:
        print("\n  ❌ Valor inválido. Digite apenas números.")


def par_ou_impar():
    """Exercício 2 — Condicional + operador módulo"""
    print("\n  📌 Exercício 2: Par ou Ímpar")
    print("  " + "-" * 38)

    try:
        numero = int(input("  Digite um número inteiro: "))

        if numero % 2 == 0:
            print(f"\n  ✅ {numero} é PAR")
        else:
            print(f"\n  ✅ {numero} é ÍMPAR")
    except ValueError:
        print("\n  ❌ Valor inválido. Digite apenas números inteiros.")


def contagem_regressiva():
    """Exercício 3 — Loop while"""
    print("\n  📌 Exercício 3: Contagem regressiva")
    print("  " + "-" * 38)

    contador = 10

    print("\n  🚀 Iniciando contagem...\n")
    while contador >= 1:
        print(f"  {contador}...")
        contador -= 1

    print("  🎉 BOOM!")


def multiplos_de_tres():
    """Exercício 4 — Loop for + operador módulo"""
    print("\n  📌 Exercício 4: Múltiplos de 3 até 30")
    print("  " + "-" * 38)

    multiplos = []

    for numero in range(1, 31):
        if numero % 3 == 0:
            multiplos.append(numero)

    print(f"\n  ✅ Múltiplos encontrados: {multiplos}")


def calcular_media():
    """Exercício 5 — Entrada de dados + operador matemático"""
    print("\n  📌 Exercício 5: Média de 3 notas")
    print("  " + "-" * 38)

    try:
        nota1 = float(input("  Digite a nota 1 (0 a 10): "))
        nota2 = float(input("  Digite a nota 2 (0 a 10): "))
        nota3 = float(input("  Digite a nota 3 (0 a 10): "))

        media = (nota1 + nota2 + nota3) / 3
        print(f"\n  ✅ Média calculada: {media:.2f}")
    except ValueError:
        print("\n  ❌ Valor inválido. Digite apenas números.")


def verificar_aprovacao():
    """Exercício 6 — Condicional encadeada"""
    print("\n  📌 Exercício 6: Verificar aprovação do aluno")
    print("  " + "-" * 38)

    try:
        nota1 = float(input("  Digite a nota 1 (0 a 10): "))
        nota2 = float(input("  Digite a nota 2 (0 a 10): "))
        nota3 = float(input("  Digite a nota 3 (0 a 10): "))

        media = (nota1 + nota2 + nota3) / 3

        print(f"\n  📊 Média: {media:.2f}")

        if media >= 7:
            print("  ✅ Situação: APROVADO(A) 🎉")
        elif media >= 5:
            print("  ⚠️  Situação: RECUPERAÇÃO")
        else:
            print("  ❌ Situação: REPROVADO(A)")
    except ValueError:
        print("\n  ❌ Valor inválido. Digite apenas números.")


def maior_numero():
    """Exercício 7 — Condicional simples"""
    print("\n  📌 Exercício 7: Maior número entre dois")
    print("  " + "-" * 38)

    try:
        a = float(input("  Digite o primeiro número: "))
        b = float(input("  Digite o segundo número:  "))

        if a > b:
            print(f"\n  ✅ O maior número é: {a}")
        elif b > a:
            print(f"\n  ✅ O maior número é: {b}")
        else:
            print(f"\n  ✅ Os dois números são iguais: {a}")
    except ValueError:
        print("\n  ❌ Valor inválido. Digite apenas números.")


def positivo_negativo_zero():
    """Exercício 8 — Condicional múltipla"""
    print("\n  📌 Exercício 8: Positivo, negativo ou zero")
    print("  " + "-" * 38)

    try:
        numero = float(input("  Digite um número: "))

        if numero > 0:
            print(f"\n  ✅ {numero} é POSITIVO ➕")
        elif numero < 0:
            print(f"\n  ✅ {numero} é NEGATIVO ➖")
        else:
            print(f"\n  ✅ O número é ZERO ⭕")
    except ValueError:
        print("\n  ❌ Valor inválido. Digite apenas números.")