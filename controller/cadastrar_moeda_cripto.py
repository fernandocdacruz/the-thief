from model.dao.dao_factory import DaoFactory

def cadastrar_moeda_cripto():
    menu_op = -1
    while menu_op != 0:
        moeda_cripto_dao = DaoFactory.create_moeda_cripto_dao()
        mostrar_moedas_cadastradas(moeda_cripto_dao)
        mostrar_menu()
        menu_op = escolher_menu_op()
        executar_menu_op(menu_op, moeda_cripto_dao)

def mostrar_moedas_cadastradas(dao):
    moedas = dao.achar_todas_moedas()
    if len(moedas) == 0:
        print("\nNenhuma moeda cadastrada ainda.")
    else:
        print("\nSegue moedas cadastradas:\n")
        for moeda in moedas:
            print(f"Id: {moeda.id} | Nome: {moeda.nome} | Sigla: {moeda.sigla}")

def mostrar_menu():
    print("\n[0] - Sair")
    print("[1] - Cadastrar nova moeda")
    print("[2] - Excluir moeda")

def escolher_menu_op():
    while True:
        try:
            menu_op = int(input("\nDigite a opção desejada: "))
            if menu_op not in [0,1,2]:
                raise ValueError("Opção inválida. Tente novamente.")
            return menu_op
        except ValueError as e:
            print(f"Erro: {e}")

def executar_menu_op(menu_op, dao):
    if menu_op == 1:
        cadastrar(dao)
    else:
        excluir(dao)

def cadastrar(dao):
    nome = obterString("\nDigite o nome da moeda: ")
    sigla = obterString("Digite a sigla da moeda: ")
    dao.adicionar_moeda(nome, sigla)
    print("\nMoeda adicionada!")

def excluir(dao):
    moedas = dao.achar_todas_moedas()
    if len(moedas) == 0:
        print("\nNenhuma moeda cadastrada ainda.")
        return

    try:
        id = int(obterString("Digite o ID da moeda a excluir: "))
    except ValueError:
        print("\nID inválido. Digite um número inteiro.")
        return

    moeda_existente = any(moeda.id == id for moeda in moedas)

    if moeda_existente:
        if dao.excluir_moeda(id):
            print("\nMoeda excluída com sucesso.")
        else:
            print("\nErro ao excluir. Verifique o ID.")
    else:
        print("\nID inexistente. Tente novamente.")

def obterString(prompt):
    while True:
        try:
            str = input(prompt).strip()
            if (not str):
                raise ValueError("Esse campo não pode ficar em branco. Tente novamente.")
            return str
        except ValueError as e:
            print(f"Erro: {e}")