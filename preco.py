# while type(monitor1) == str:
#     print("INFORME O VALOR EM NUMERO")
#     monitor1=input()
#     if type(monitor1) == int or type(monitor1) == float:
#     	break
import sys
print("Qual o valor do Monitor Primario?")
try:
	monitor1=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		monitor1=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor do Monitor Secundario?")
try:
	monitor2=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		monitor2=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor do Gabinete?")
try:
	gabinete=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		gabinete=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor da placa de video?")
try:
	placa_video=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		placa_video=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor da placa mae?")
try:
	placa_mae=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		placa_mae=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor da memoria?(Se for mais que um, colocar o valor da soma das duas")
try:
	memoria=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		memoria=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor da fonte de energia?")
try:
	fonte=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		fonte=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

print("Qual o valor do Processador?")
try:
	processador=float(input())
except ValueError:
	print("Voce não informou um valor valido , tente novamente por favor")
	try:
		processador=float(input())
	except ValueError:
		print("Voce não informou um valor valido.Abra o software novamente")
		sys.exit()

total = monitor2+monitor1+memoria+placa_mae+placa_video+fonte+processador+gabinete

print(f"Monitor Primario ---------- R${monitor1:5.2f}")
print(f"Monitor Secundario -------- R${monitor2:5.2f}")
print(f"processador --------------- R${processador:5.2f}")
print(f"Gabinete ------------------ R${gabinete:5.2f}")
print(f"Placa de Video ------------ R${placa_video:5.2f}")
print(f"Placa mãe ----------------- R${placa_mae:5.2f}")
print(f"Memoria ------------------- R${memoria:5.2f}")
print(f"Fonte --------------------- R${fonte:5.2f}")
print("------------------------------------")
print(f"\nTOTAL ------------------- R${total:5.2f}")