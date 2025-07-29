from model.entities.carteira import Carteira
from model.entities.moeda_cripto import MoedaCripto
from model.entities.posicao import Posicao
from model.entities.usuario import Usuario


class PosicaoDao:
    def __init__(self, connection):
        self.conn = connection

    def criar_posicao(self, carteira_id, compra_dolar, moeda_cripto, total_compra_moeda_investida):
        sql = ("INSERT INTO posicao (carteira_id, compra_dolar, moeda_investida, total_compra_moeda_investida) "
                + "VALUES (%s, %s, %s, %s)")

        with self.conn.cursor() as cursor:
            cursor.execute(sql, (carteira_id, compra_dolar, moeda_cripto, total_compra_moeda_investida))
            self.conn.commit()

    def listar_todas_posicoes(self):
        posicoes = []
        sql = """
              SELECT p.id AS posicao_id, 
                     p.abertura, 
                     p.status, 
                     p.encerramento, 
                     p.compra_dolar, 
                     p.total_compra_moeda_investida, 

                     c.id AS carteira_id, 

                     u.id AS usuario_id, 
                     u.login, 
                     u.senha, 

                     m.id AS moeda_id, 
                     m.nome, 
                     m.sigla

              FROM posicao p
                       JOIN carteira c ON p.carteira_id = c.id
                       JOIN usuario u ON c.usuario_id = u.id
                       JOIN moedas m ON p.moeda_investida = m.id
              WHERE p.status = %s 
              """

        with self.conn.cursor(dictionary=True) as cursor:  # <- `dictionary=True` facilita a leitura
            cursor.execute(sql, ('Aberta',))
            resultados = cursor.fetchall()

            for row in resultados:
                usuario = Usuario(
                    id=row["usuario_id"],
                    login=row["login"],
                    senha=row["senha"]
                )
                carteira = Carteira(
                    id=row["carteira_id"],
                    usuario=usuario
                )
                moeda = MoedaCripto(
                    id=row["moeda_id"],
                    nome=row["nome"],
                    sigla=row["sigla"]
                )
                posicao = Posicao(
                    id=row["posicao_id"],
                    carteira=carteira,
                    abertura=row["abertura"],
                    status=row["status"],
                    encerramento=row["encerramento"],
                    compra_dolar=row["compra_dolar"],
                    moeda_cripto=moeda,
                    total_compra_moeda_investida=row["total_compra_moeda_investida"]
                )
                posicoes.append(posicao)

        return posicoes
