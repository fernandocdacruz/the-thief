class CotacaoMoeda:
    def __init__(self, id: int, moeda, valor: float, datahora_cotacao=None):
        self.id = id
        self.moeda = moeda
        self.valor = valor
        self.datahora_cotacao = datahora_cotacao