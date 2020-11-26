nome_cliente = str(input("\nInsira o nome do cliente: -> "))
ocorrencia = str(input("\nInsira a ocorrencia: -> "))
data = str(input("\nInsira a data da ocorrencia: -> "))
status = str(input("\nInsira o status da ocorrencia: -> "))



total =f"❗{nome_cliente} - {ocorrencia}\n📆Data da Solicitação: ```{data}```\n📌Status: *{status}*"


arquivo = open("whatsapp.txt","a",encoding="utf-8")
arquivo.write("\n\n"+total+"\n\n\n")
arquivo.close()