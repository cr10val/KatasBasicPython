#Katas Basic Python - Ejercicio 6

ini =  int(input("Introduzca el inicio: "))
fin = int(input("Introduzca el fin: "))


for x in range(ini, fin + 1):
    if x % 2 != 0:
        print(x)

