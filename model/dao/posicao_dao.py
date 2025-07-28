class PosicaoDao:
    def __init__(self, connection):
        self.conn = connection

    def criar_posicao(self, carteira_id, compra_dolar, moeda_cripto, total_compra_moeda_investida):
        sql = ("INSERT INTO posicao (carteira_id, compra_dolar, moeda_investida, total_compra_moeda_investida) "
                + "VALUES (%s, %s, %s, %s)")

        with self.conn.cursor() as cursor:
            cursor.execute(sql, (carteira_id, compra_dolar, moeda_cripto, total_compra_moeda_investida))
            self.conn.commit()