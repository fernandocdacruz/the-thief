import requests

class MoedaCripto:
    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def obter_valor_usd(self):
        nome_formatado = self.nome.lower()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={nome_formatado}&vs_currencies=usd"
        response = requests.get(url)

        if response.status_code == 200:
            preco_usd = response.json().get(nome_formatado, {}).get("usd", 0)
        else:
            preco_usd = 0
            print(f"Erro ao buscar cotação de {self.nome}: {response.status_code}")

        return preco_usd
