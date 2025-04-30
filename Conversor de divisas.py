#integrantes Mortola S. Costantini M. Repka M.
import datetime

# Valor de divisas como diccionario
divisas = {
    'USD': 1,
    'EUR': 0.88,
    'ARS': 1150,
    'BRL': 5.62
}

# Inputs
plata_tot = float(input("¿Cuánto dinero desea convertir? "))
plata_act = input("¿Que moneda posee (USD, EUR, ARS, BRL)? ").upper()
plata_nue = input("¿A que moneda desea hacer la conversión (USD, EUR, ARS, BRL)? ").upper()

if plata_act == 'USD':
 num = divisas['USD']
if plata_act == 'EUR':
 num = divisas['EUR']
if plata_act == 'ARS':
 num = divisas['ARS']
if plata_act == 'BRL':
 num = divisas['BRL']

if plata_nue == 'USD':
 den = divisas['USD']
if plata_nue == 'EUR':
 den = divisas['EUR']
if plata_nue == 'ARS':
 den = divisas['ARS']
if plata_nue == 'BRL':
 den = divisas['BRL']

# Calculo de resultado e impresion por pantalla
resultado = plata_tot * (den/num)
print("El total convertido es de ", resultado, " ", plata_nue)

# Guardar en archivo txt
with open("historial.txt", "a") as archivo:
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo.write(f"{fecha} - {plata_tot} {plata_act} -> {resultado:.2f} {plata_nue}\n")

# Borrar historial
opcion = input("¿Desea Borrar el historial?").lower()
if opcion == 'si':
 with open("historial.txt", "w") as archivo:
    archivo.write("")