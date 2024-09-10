edad = int(input("Escribe tu edad "))
ingresos = int(input("Escribe el valor de tus ingresos mensuales "))
if edad >= 18 and ingresos >= 3000000:
    print ("Debes pagar impuestos")
else:
    print("No debes pagar nada :) ")