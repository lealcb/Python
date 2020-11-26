import requests

print("Digite o MAC do produto")
mac = input("->")

request = requests.get(f"https://api.macvendors.com/{mac}")

print(request.text)

