#Kata Basic Python
import random
"""
Ejercicio 10
Nuestro objetivo es adivinar el numero. Si fallamos 
nos diran si es mayor o menor que el numero buscado.
Tambien poner el numero de intentos requeridos
"""


num = random.randint(1,100)
it= x = 0
while x != num:
    it += 1
    x = int(input("Introduzca un numero entre 1 y 100: "))
    if num > x:
        print("El numero buscado es mayor")
    elif num < x:
        print("El numero buscado es menor")
    else:
        print("HA ACERTADO en ", it, " intentos")




