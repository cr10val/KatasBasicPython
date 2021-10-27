#RetoIII
"""Reto 3
   Carta de Restaurante

El ejercicio consiste en crear un programa que muestre por consola la carta de un restaurante
donde añadiremos diferentes platos y después escogeremos que queramos para comer. Una
vez hecha esto se tendrá que calcular el precio de la comida, el programa nos tiene que decir
con qué billetes y monedas tenemos que pagar.

"""
#Modenas y Billetes
#TODO Meterlo en una tupla
"""
1. Crear una variable de tipo entero por cada uno de los billetes que existen desde 5€ a 500€,
además de esto tendréis que crear otra variable para guardar el precio total de la comida.
"""
dinero = [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500]

"""
2. Crear dos arrays, uno donde guardaremos el menú y otro donde guardaremos el precio de
cada plato.
"""
#menu = []
#precios = []
#en vez de dos arrays, utilizamos un diccionario
menu = {}
comanda = []
importe = 0

#Pide el num de platos que se quieren pedir
num_platos = int(input("Cuantos platos quiere añadir?"))
"""
Con un bucle for tendremos que llenar los dos arrays anteriormente creados. Añadiremos el
nombre del plato y después el precio. Puedes crear un diccionario de datos (investiga al
respecto).
"""
i=1
#Solicita los platos y precios el numero de veces que se ha indicado
for i in range(num_platos):
    #menu.append(input("Introduzca nombre del plato "+str(i)+": "))
    #precios.append(int(input("Ahora introduzca el precio "+str(i)+": ")))
    plato = input("Introduzca nombre del plato "+str(i)+": ")
    precio = int(input("Ahora introduzca el precio "+str(i)+": "))
    menu[plato] = precio

print(menu)
#print (precios)


pedir=""
#Repite la pregunta hasta que se responda S o N
while pedir != "N" and pedir != "S":
    pedir = input("Quiere pedir la comida? (S/N) ")

#Mientras se quiere pedir, se pregunta el nombre del plato
while pedir == "S":
    comanda.append(input("Introduzca el nombre del plato: "))
    pedir = ""    
    #Repite la pregunta hasta que se responda S o N
    while pedir != "N" and pedir != "S":
        pedir = input("Quiere seguir pidiendo? (S/N) ")
    
i=0
#Recorre la lista de comanda, para calcular el importe
for i in range(len(comanda)):
    #Si NO existe el plato en el menu
    if comanda[i] not in menu: #menu.count(comanda[i]) == 0 :
        print("El siguiente plato no existe: ", comanda[i])
    else:  # Si existe, busca el precio y lo suma              
        #importe += precios[menu.index(comanda[i])]
        importe += menu[comanda[i]]

print("EL total de la cuenta es: ", importe )

#Esto creo que esta mal planteado, habria que saber que monedas y billetes tiene para pagar
#De momento lo dejamos con el minimo numero de billetes
#TODO 
print("Para pagar con el menur numero de billetes/monedas deberia usar: ")
resto = importe
while resto > 0:
    i=0
    while dinero[i] < resto:
        i += 1
    print (" 1 de ", dinero[i])
    resto -= dinero[i]    

