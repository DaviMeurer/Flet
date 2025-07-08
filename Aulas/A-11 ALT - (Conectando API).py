import requests

url = "https://open.er-api.com/v6/latest/USD"

resposta = requests.get(url)

if resposta.status_code==200:
    dados = resposta.json()
    print(dados["rates"]["BRL"])