import mysql.connector
from model.entities.moeda_cripto import MoedaCripto

class UsuarioCriptoDao:

    def __init__(self, connection):
        self.conn = connection

    def achar_todas_moedas(self):
        moedas = []
        sql = "SELECT id, nome, sigla FROM moedas"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            resultados = cursor.fetchall()
            for row in resultados:
                moeda = MoedaCripto(id=row[0], nome=row[1], sigla=row[2])
                moedas.append(moeda)
            return moedas

    def adicionar_moeda(self, nome, sigla):
        sql = "INSERT INTO moedas (nome, sigla) VALUES (%s, %s)"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (nome, sigla))
            self.conn.commit()

    def excluir_moeda(self, id):
        sql = "DELETE FROM moedas WHERE id = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (id, ))
            self.conn.commit()