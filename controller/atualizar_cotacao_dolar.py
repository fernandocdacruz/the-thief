from model.dao.dao_factory import DaoFactory

def atualizar_cotacao_dolar():
    cotacao_dolar_dao = DaoFactory.create_cotacao_dolar_dao()
    menu_op = -1
    while menu_op != 0:

        mostrar_cotacao_atual(cotacao_dolar_dao)
        menu()
        menu_op = escolher_menu_op()
        executar_menu_op(menu_op, cotacao_dolar_dao)

def mostrar_cotacao_atual(dao):
    cotacao_atual = dao.cotacao_atual_dolar()

    if not cotacao_atual:
        print("\nNão há nenhum valor de cotação disponível.")
    else:
        data_formatada = cotacao_atual.data.strftime("%d/%m/%Y")
        print(f"\nCotação atual: R$ {cotacao_atual.valor:.2f} | {data_formatada}")

def menu():
    print("\n[0] - Sair")
    print("[1] - Adicionar cotação")

def escolher_menu_op():
    while True:
        try:
            menu_op = int(input("\nDigite a opção desejada: "))
            if menu_op not in [0,1]:
                raise ValueError("\nOpção inválida. Tente novamente.")
            return menu_op
        except ValueError as e:
            print(f"Erro: {e}")

def executar_menu_op(menu_op, dao):
    if menu_op == 1:
        adicionar_cotacao(dao)

def adicionar_cotacao(dao):
    try:
        valor = float(input("\nDigite o valor do dolar hoje: "))
        dao.adicionar_cotacao_dolar(valor)
        print("\nValor adicionado!")
    except ValueError as e:
        print("\nValor inválido. Tente novamente.")