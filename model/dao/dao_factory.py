from db.connection_factory import DB
from model.dao.moeda_cripto_dao import MoedaCriptoDao
from model.dao.posicao_dao import PosicaoDao
from model.dao.usuario_dao import UsuarioDao


class DaoFactory:
    @staticmethod
    def create_usuario_dao():
        conn = DB.get_connection()
        return UsuarioDao(conn)
    @staticmethod
    def create_moeda_cripto_dao():
        conn = DB.get_connection()
        return MoedaCriptoDao(conn)
    @staticmethod
    def create_posicao_dao():
        conn = DB.get_connection()
        return PosicaoDao(conn)
