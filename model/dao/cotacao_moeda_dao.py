import mysql.connector
from model.entities.moeda_cripto import MoedaCripto


class CotacaoMoedaDao():
    def __init__(self, connection):
        self.conn = connection

    def adicionar_cotacao(self, moeda: MoedaCripto, valor):
        sql = "INSERT INTO cotacao_moedas (moeda_id, valor) VALUES (%s, %s)"
        with self.conn.cursor() as cursor:
            cursor.execute(sql, (moeda.id, valor))
        self.conn.commit()
