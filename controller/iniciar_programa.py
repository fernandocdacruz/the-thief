from controller.cadastrar_moeda_cripto import cadastrar_moeda_cripto


def iniciar_programa():
    op_menu = -1
    while op_menu != 0:
        menu()
        op_menu = obter_op_menu()
        executar_op(op_menu)

def menu():
    print("\n[0] - Sair")
    print("[1] - Cadastrar nova moeda cripto ")

def obter_op_menu():
    while True:
        try:
            op = input("\nOP: ")
            validar_op(op)
            return int(op)
        except ValueError as e:
            print(f"\nErro: {e}")

def validar_op(op):
    if not op:
        raise ValueError("Input em branco. Tente novamente.")
    int_op = int(op)
    if int_op not in [0,1]:
        raise ValueError("Opção inválida. Tente novamente.")

def executar_op(op: int):
    if op == 1:
        cadastrar_moeda_cripto()

