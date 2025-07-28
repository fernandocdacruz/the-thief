from model.dao import posicao_dao
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
    moeda = obter_moeda(dao)
    valor_compra_moeda = obter_valor_compra_moeda()
    carteira_id = 1
    posicao_dao = DaoFactory.create_posicao_dao()
    posicao_dao.criar_posicao(carteira_id, valor_compra_dolar, moeda.id, valor_compra_moeda)
    print("\nPosição criada !!")

def obter_valor_compra_moeda():
    while True:
        try:
            entrada = input("\nDigite o valor total da compra da moeda: ").replace(',', '.')
            valor = float(entrada)
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("\nValor inválido. Tente novamente.")


def obter_moeda(dao):
    moeda = None
    while True:
        try:
            id_moeda = int(input("\nDigite o ID da moeda: "))
            moeda = dao.achar_moeda_id(id_moeda)
            if moeda == None:
                raise ValueError("\nID inválido. Tente novamente.")
            return moeda
        except ValueError:
            print("\nInput inválido. Tente novamente.")

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
