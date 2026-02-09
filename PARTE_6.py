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
