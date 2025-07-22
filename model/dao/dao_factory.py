from db.connection_factory import DB
from model.dao.moeda_cripto_dao import UsuarioCriptoDao
from model.dao.usuario_dao import UsuarioDao


class DaoFactory:
    @staticmethod
    def create_usuario_dao():
        conn = DB.get_connection()
        return UsuarioDao(conn)
    @staticmethod
    def create_moeda_cripto_dao():
        conn = DB.get_connection()
        return UsuarioCriptoDao(conn)