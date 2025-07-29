from model.entities.moeda_cripto import MoedaCripto


class Posicao:
    def __init__(self, id, carteira, abertura, status, encerramento, compra_dolar, moeda_cripto: "MoedaCripto",
                 total_compra_moeda_investida):
        self.id = id
        self.carteira = carteira
        self.abertura = abertura
        self.status = status
        self.encerramento = encerramento
        self.compra_dolar = compra_dolar
        self.moeda_cripto = moeda_cripto
        self.total_compra_moeda_investida = total_compra_moeda_investida

    def resumo(self):
        #jogar ataualização da cotação aqui
        print(f"{self.abertura} | US$ {self.compra_dolar} | {self.moeda_cripto.sigla} | {self.total_compra_moeda_investida} |")