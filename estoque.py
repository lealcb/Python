import math

try:
	print("Qual o estoque:")
	estoque = float(input("-> "))
	print("Qual o estoque KG:")
	estoque2 = float(input("->"))
except:
	print("Não digitou um valor invalido , coloque valor tipo float")
	estoque=float(input("-> "))
unidadecx24 = 24
unidadecx12 = 12
unidadecx6  = 6
unidadecx7  = 7
unidadekg   = 1.5
cx24 = estoque/unidadecx24
cx12 = estoque/unidadecx12
cx6  = estoque/unidadecx6
cx7  = estoque/unidadecx7
kg   = estoque2/unidadekg


# def numero_depois_do_decimal(estoque):
    
#     numero = str(estoque)
#     if 'e-' in numero: 
#         numero_float = format(float(numero), '.%df'%(len(numero.split(".")[1].split("e-")[0])+int(numero.split('e-')[1])))
#         l = list(str(number_float))
#         l.insert(1, ".")
#         number_float = "".join(l)
#     elif "." in numero: 
#         number_float = numero.split(".")[1]
#         l = list(str(number_float))
#         l.insert(1, ".")
#         number_float = "".join(l)
#     return  number_float
	
# restocx24 = float(numero_depois_do_decimal(cx24))*24
# teste24 = c
# restocx12 = float(numero_depois_do_decimal(cx12))*12
# restocx6 = float(numero_depois_do_decimal(cx6))*6
# restocx4 = float(numero_depois_do_decimal(cx4))*4



restocx24 = (int(cx24)*unidadecx24-estoque)*-1
restocx12 = (int(cx12)*unidadecx12-estoque)*-1
restocx6 =  (int(cx6)*unidadecx6-estoque)*-1
restocx7 =  (int(cx7)*unidadecx7-estoque)*-1
restokg =  (int(kg)*unidadekg-estoque2)*-1





print(f"Estoque: {estoque:5.0f} Unidades")
print(f"Estoque: {estoque2:5.0f} Quilos")
print(f"Estoque: {cx24:5.0f} Caixas com 24 e {restocx24:5.0f} Unidades ")
print(f"Estoque: {cx12:5.0f} Caixas com 12 e {restocx12:5.0f} Unidades")
print(f"Estoque: {cx6:5.0f} Caixas com 6  e {restocx6:5.0f}  Unidades")
print(f"Estoque: {cx7:5.0f} Caixas com 7 unidades  e {restocx7:5.0f}  Unidades")
print(f"Estoque: {kg:5.0f} Sacos com 1.5KG  e {restokg:5.0f}  KG do saco principal")