renta = float(input("Ingrese el valor de su renta anual "))
if renta <= 1000000:
    print ("Su impositivo es de 5%")
elif renta >1000000 and renta <= 2000000:
    print ("Su impositivo es de 15%")
elif renta >2000000 and renta <= 3500000:
    print ("Su impositivo es de 20%")
elif renta >3500000 and renta <= 6000000:
    print ("Su impositivo es de 30%")
elif renta > 6000000:
    print ("Su impositivo es de 45%")                    