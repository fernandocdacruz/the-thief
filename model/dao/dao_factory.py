from db.connection_factory import DB
from model.dao.cotacao_dolar_dao import CotacaoDolarDao
from model.dao.cotacao_moeda_dao import CotacaoMoedaDao
from model.dao.moeda_cripto_dao import MoedaCriptoDao
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
    def create_cotacao_dolar_dao():
        conn = DB.get_connection()
        return CotacaoDolarDao(conn)
    @staticmethod
    def create_cotacao_moeda_dao():
        conn = DB.get_connection()
        return CotacaoMoedaDao(conn)