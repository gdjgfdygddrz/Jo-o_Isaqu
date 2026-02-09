while True:
    print("\n===== CALCULADORA =====")
    print("+  Soma")
    print("-  Subtração")
    print("*  Multiplicação")
    print("/  Divisão")
    print("0  Sair")
    print("======================")

    opcao = input("Escolha a operação: ").strip()

    if opcao == "0":
        print("Programa encerrado 👋")
        break

    if opcao not in operacoes:
        print("Opção inválida!")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: digite apenas números!")
        continue

    resultado = operacoes[opcao](num1, num2)
    print("Resultado:", resultado)
