edad = int(input("Ingrese su edad "))
if edad >=0 and edad < 4:
    print ("Debe pagar una tarifa de $0 entra GRATIS")
elif edad >=4 and edad <= 18:
    print("Debe pagar una tarifa de $5000")
elif edad > 18:
    print ("Debe pagar una tarifa de $10000")         