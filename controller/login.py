from controller.iniciar_programa import iniciar_programa
from model.dao.dao_factory import DaoFactory
from model.dao.usuario_dao import UsuarioDao
from db.connection_factory import DB

def realizar_login():
    if escolher_op() == 0:
        return 0
    else:
        usuario_dao = DaoFactory.create_usuario_dao()
        login = obter_string("\nLOGIN: ")
        usuario = usuario_dao.achar_pelo_login(login)
        if usuario == None:
            print("\nUsuário inválido")
        else:
            senha = obter_string("SENHA: ")
            if usuario.senha == senha:
                print("\nLogin realizado com sucesso.")
                iniciar_programa()
            else:
                print("\nSenha inválida.")

def escolher_op():
    while True:
        try:
            login_menu_op = int(input("\nDigite 0 para sair ou 1 para login: "))
            if login_menu_op not in [0,1]:
                raise ValueError("\nOpção inválida. Tente novamente.")
            return login_menu_op
        except ValueError as e:
            print(f"Erro: {e}")

def obter_string(prompt: str):
    while True:
        try:
            valor = input(prompt).strip()
            validar_str(valor)
            return valor
        except ValueError as e:
            print(f"Erro: {e}")

def validar_str(valor: str):
    if not valor:
        raise ValueError("\nInput inválido. Tente novamente.")