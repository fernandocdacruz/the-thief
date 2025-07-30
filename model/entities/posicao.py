class Posicao:
    def __init__(self, id, carteira, abertura, status, encerramento, compra_dolar, moeda_cripto, total_compra_moeda_investida):
        self.id = id
        self.carteira = carteira
        self.abertura = abertura
        self.status = status
        self.encerramento = encerramento
        self.compra_dolar = compra_dolar
        self.moeda_cripto = moeda_cripto  # objeto com nome e quantidade
        self.total_compra_moeda_investida = total_compra_moeda_investida

    def resumo(self):
        preco_usd = self.moeda_cripto.obter_valor_usd()
        valor_atual = preco_usd * self.total_compra_moeda_investida
        lucro = valor_atual - self.compra_dolar
        percentual = (lucro / self.compra_dolar) * 100 if self.compra_dolar != 0 else 0

        return (f"\t{self.id} | {self.abertura} | US$ {self.compra_dolar:.2f} | {self.moeda_cripto.nome.upper()} | "
                f"{self.total_compra_moeda_investida:.10f} | Valor Atual: ${valor_atual:.2f} | "
                f"Lucro: ${lucro:.2f} | %: {percentual:.2f}%")



