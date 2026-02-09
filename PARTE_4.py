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
