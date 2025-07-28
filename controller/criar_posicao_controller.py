from model.dao import moeda_cripto_dao
from model.dao.dao_factory import DaoFactory

def criar_posicao():
    menu_op = -1
    moeda_cripto_dao = DaoFactory.create_moeda_cripto_dao()
    while menu_op != 0:
        mostrar_menu()
        menu_op = escolher_menu_op()
        executar_menu_op(menu_op, moeda_cripto_dao)

def mostrar_menu():
    print("\n[0] - Sair")
    print("[1] - Criar posição")

def escolher_menu_op():
    while True:
        try:
            menu_op = int(input("\nDigite a opção desejada: "))
            if menu_op not in [0,1]:
                raise ValueError("\nOpção inválida. Tente novamente.")
            return menu_op
        except ValueError as e:
            print(f"Erro: {e}")

def executar_menu_op(menu_op: int, dao):
    if menu_op == 1:
        criar(dao)

def criar(dao):
    mostrar_moedas_cadastradas(dao)
    valor_compra_dolar = obter_valor_compra_dolar()

def obter_valor_compra_dolar():
    while True:
        try:
            valor = float(input("\nDigite o valor da compra: "))
            return valor
        except ValueError as e:
            print("\nValor inválido. Tente novamente.")

def mostrar_moedas_cadastradas(dao):
    moedas = dao.achar_todas_moedas()
    if len(moedas) == 0:
        print("\nNenhuma moeda cadastrada ainda.")
    else:
        print("\nSegue moedas cadastradas:\n")
        for moeda in moedas:
            print(f"Id: {moeda.id} | Nome: {moeda.nome} | Sigla: {moeda.sigla}")
