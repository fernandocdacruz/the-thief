from model.dao.dao_factory import DaoFactory

def mostrar_carteira():
    posicao_dao = DaoFactory.create_posicao_dao()
    posicoes = posicao_dao.listar_todas_posicoes()
    if len(posicoes) == 0:
        print("\nNão há nenhuma posição na sua carteira ainda.")
    else:
        for posicao in posicoes:

