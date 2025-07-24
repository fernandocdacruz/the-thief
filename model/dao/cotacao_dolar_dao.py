import mysql.connector

from model.entities.cotacao_dolar import CotacaoDolar


class CotacaoDolarDao:
    def __init__(self, connection):
        self.conn = connection

    def cotacao_atual_dolar(self):
        sql = "SELECT * FROM cotacao_dolar ORDER BY id DESC LIMIT 1"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                return CotacaoDolar (id=row[0], valor=row[1], data=row[2])
            return None

    def adicionar_cotacao_dolar(self, valor):
        sql = "INSERT INTO cotacao_dolar(valor) VALUES (%s)"
        with self.conn.cursor() as cursor:
            cursor.execute(sql,(valor,))
            self.conn.commit()

