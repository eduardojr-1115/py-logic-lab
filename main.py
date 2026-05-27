# ============================================================
#  main.py — Ponto de entrada do projeto
#  Projeto: py-logic-lab | Rocketseat Style
# ============================================================

import exercicios


# ---------- Cabeçalho visual do terminal ----------

def exibir_cabecalho():
    print()
    print("  ╔══════════════════════════════════════╗")
    print("  ║       🚀  py-logic-lab               ║")
    print("  ║   Exercícios de Lógica em Python     ║")
    print("  ║        Rocketseat Style 🔥           ║")
    print("  ╚══════════════════════════════════════╝")
    print()


# ---------- Menu principal ----------

def exibir_menu():
    print("  ┌──────────────────────────────────────┐")
    print("  │          ESCOLHA UM EXERCÍCIO        │")
    print("  ├──────────────────────────────────────┤")
    print("  │  1 → Somar dois números              │")
    print("  │  2 → Par ou Ímpar                   │")
    print("  │  3 → Contagem regressiva             │")
    print("  │  4 → Múltiplos de 3 até 30           │")
    print("  │  5 → Calcular média de 3 notas       │")
    print("  │  6 → Verificar aprovação             │")
    print("  │  7 → Maior número entre dois         │")
    print("  │  8 → Positivo, negativo ou zero      │")
    print("  ├──────────────────────────────────────┤")
    print("  │  0 → Sair                            │")
    print("  └──────────────────────────────────────┘")
    print()


# ---------- Roteador de exercícios ----------

def executar_exercicio(opcao):
    """Direciona para o exercício escolhido pelo usuário."""

    rotas = {
        "1": exercicios.somar_dois_numeros,
        "2": exercicios.par_ou_impar,
        "3": exercicios.contagem_regressiva,
        "4": exercicios.multiplos_de_tres,
        "5": exercicios.calcular_media,
        "6": exercicios.verificar_aprovacao,
        "7": exercicios.maior_numero,
        "8": exercicios.positivo_negativo_zero,
    }

    funcao = rotas.get(opcao)

    if funcao:
        funcao()
    else:
        print("\n  ❌ Opção inválida. Escolha um número de 0 a 8.")


# ---------- Loop principal ----------

def main():
    exibir_cabecalho()

    while True:
        exibir_menu()

        opcao = input("  👉 Digite sua opção: ").strip()

        if opcao == "0":
            print()
            print("  👋 Até mais! Bons estudos na jornada! 🚀")
            print()
            break

        executar_exercicio(opcao)

        print()
        input("  ↩  Pressione ENTER para voltar ao menu...")
        print("\n" + "=" * 44 + "\n")


# ---------- Execução ----------

if __name__ == "__main__":
    main()