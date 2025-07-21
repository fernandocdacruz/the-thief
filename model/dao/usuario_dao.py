from model.entities.usuario import Usuario
import mysql.connector

class UsuarioDao:

    def __init__(self, connection):
        self.conn = connection

    def achar_pelo_login(self, login):
        sql = "SELECT id, login, senha FROM usuario WHERE login = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (login,))
            row = cursor.fetchone()
            if row:
                return Usuario(id=row[0], login=row[1], senha=row[2])
            return None