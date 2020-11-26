import requests

print("Digite o CEP:")
cep = input("->")

request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

print(request.text)

