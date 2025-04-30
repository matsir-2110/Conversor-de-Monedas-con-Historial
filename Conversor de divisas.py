#integrantes Mortola S. Costantini M. Repka M.

# Valor de divisas
USD = 1
EUR = 0.88
ARS = 1150
BRL = 5.62

# Inputs
plata_tot = float(input("¿Cuánto dinero desea convertir? "))
plata_act = input("¿Que moneda posee (USD, EUR, ARS, BRL)? ").upper()
plata_nue = input("¿A que moneda desea hacer la conversión (USD, EUR, ARS, BRL)? ").upper()

if plata_act == 'USD':
 num = USD
if plata_act == 'EUR':
 num = EUR
if plata_act == 'ARS':
 num = ARS
if plata_act == 'BRL':
 num = BRL
plata_nue
if plata_nue == 'USD':
 den = USD
if plata_nue == 'EUR':
 den = EUR
if plata_nue == 'ARS':
 den = ARS
if plata_nue == 'BRL':
 den = BRL

# Calculo de resultado e impresion por pantalla
resultado = plata_tot * (num/den)
print("El total convertido es de ", resultado, " ", plata_nue)

