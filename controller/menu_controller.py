from controller.cadastrar_moeda_cripto_controller import cadastrar_moeda_cripto
from controller.criar_posicao_controller import criar_posicao
import requests

def iniciar_programa():

    cotacao_usd_brl = buscar_cotacao_usd_brl()

    op_menu = -1
    while op_menu != 0:
        print(f"\nCotação USD/BRL: {cotacao_usd_brl}")
        valor_total_carteira = float(100)
        print(f"Valor total da carteira(USD): {valor_total_carteira:.2f}")
        menu()
        op_menu = obter_op_menu()
        executar_op(op_menu)

def menu():
    print("\n[0] - Sair")
    print("[1] - Cadastrar nova moeda cripto ")
    print("[2] - Mostrar carteira")

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
    if int_op not in [0,1,2,3,4]:
        raise ValueError("Opção inválida. Tente novamente.")

def executar_op(op: int):
    if op == 1:
        cadastrar_moeda_cripto()
    elif op == 2:
        criar_posicao()

def buscar_cotacao_usd_brl():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=brl"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("usd", {}).get("brl", 0)
    else:
        print("Erro ao buscar cotação do dólar:", response.status_code)
        return 0