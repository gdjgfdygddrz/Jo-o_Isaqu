# ===============================
# PARTE 1 — LÓGICA MATEMÁTICA
# ===============================

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


# ===============================
# PARTE 2 — REGISTRO DE OPERAÇÕES
# ===============================

OPERACOES = {
    "+": soma,
    "-": subtracao,
    "*": multiplicacao,
    "/": divisao
}


# ===============================
# PARTE 3 — INTERFACE (MENU)
# ===============================

def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("+  Soma")
    print("-  Subtração")
    print("*  Multiplicação")
    print("/  Divisão")
    print("0  Sair")
    print("=======================")


# ===============================
# PARTE 4 — ENTRADAS DO USUÁRIO
# ===============================

def ler_operacao():
    return input("Escolha a operação: ").strip()


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: digite apenas números!")


# ===============================
# PARTE 5 — EXECUÇÃO DA OPERAÇÃO
# ===============================

def executar_operacao(opcao, a, b):
    return OPERACOES[opcao](a, b)


# ===============================
# PARTE 6 — CONTROLE PRINCIPAL
# ===============================

def main():
    while True:
        mostrar_menu()
        opcao = ler_operacao()

        if opcao == "0":
            print("Programa encerrado 👋")
            break

        if opcao not in OPERACOES:
            print("Opção inválida!")
            continue

        num1 = ler_numero("Digite o primeiro número: ")
        num2 = ler_numero("Digite o segundo número: ")

        resultado = executar_operacao(opcao, num1, num2)
        print("Resultado:", resultado)


# ===============================
# PONTO DE ENTRADA DO PROGRAMA
# ===============================

main()
