dieta = input("Es usted vegetariano? si/no ")
if dieta == "si":
    ingrediente=input("Escoja entre: Pimiento y tofu ")
    print ("Pizza vegetariana")
    print ("Los ingredientes de su pizza son:")
    print ("Mozzarella")
    print ("Tomate")
    print(ingrediente)
elif dieta == "no":
    ingrediente=input("Escoja entre: Peperoni, jamon y salmon ")
    print ("Pizza normal")
    print ("Los ingredientes de su piza son:")
    print ("Mozzarella")
    print ("Tomate")
    print(ingrediente)
else: 
    print ("dato invalido")    
