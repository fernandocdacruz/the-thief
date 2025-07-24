from controller.atualizar_cotacao_dolar import adicionar_cotacao
from controller.cadastrar_moeda_cripto import executar_menu_op
from model.dao.dao_factory import DaoFactory

def atualizar_cotacao_cripto():

    moeda_cripto_dao = DaoFactory.create_moeda_cripto_dao()
    menu_op = -1

    while menu_op != 0:
        moedas = moeda_cripto_dao.achar_todas_moedas()
        listar_moedas(moedas)
        mostrar_menu()
        menu_op = escolher_menu_op()
        executar_menu_op(menu_op, moeda_cripto_dao)

def listar_moedas(moedas):
    if len(moedas) == 0:
        print("Não há nenhuma moeda cadastrada ainda.")
    else:
        print()
        for moeda in moedas:
            print(f"Id: {moeda.id} | Nome: {moeda.nome} | Sigla: {moeda.sigla}")

def mostrar_menu():
    print("\n[0] - Sair")
    print("[1] - Adicionar cotação")

def escolher_menu_op():
    while True:
        try:
            menu_op = int(input("\nDigite a opção desejada: "))
            if menu_op not in [0,1]:
                raise ValueError("\nOpção inválida. Tente novamente")
            return menu_op
        except ValueError as e:
            print(f"Erro: {e}")

def executar_menu_op(menu_op, dao):
    if menu_op == 1:
        adicionar_cotacao(dao)

def adicionar_cotacao(dao):
    cripto_id = obter_cripto_id(dao)
    moeda = dao.achar_moeda_id(cripto_id)
    valor_cotacao = obter_valor_cotacao()
    cotacao_moeda_dao = DaoFactory.create_cotacao_moeda_dao()
    cotacao_moeda_dao.adicionar_cotacao(moeda, valor_cotacao)
    print("\n Cotação adicionada com sucesso!")

def obter_valor_cotacao():
    while True:
        try:
            valor_str = input("Digite o valor da cotação: ").strip()
            valor_str = valor_str.replace(",", ".")
            valor = float(valor_str)
            if valor <= 0:
                print("\nO valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("\nValor inválido. Digite um número válido.")


def obter_cripto_id(dao):
    while True:
        try:
            cripto_id = int(input("\nDigite o ID da moeda: "))
            ids_disponiveis = listar_ids_cripto(dao)
            if cripto_id not in ids_disponiveis:
                raise ValueError("\nId inexistente. Tente novamente")
            return  cripto_id
        except ValueError as e:
            print(f"Erro: {e}")

def listar_ids_cripto(dao):
    moedas = dao.achar_todas_moedas()
    ids_disponiveis = []
    for moeda in moedas:
        ids_disponiveis.append(moeda.id)
    return ids_disponiveis


