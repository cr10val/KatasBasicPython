#Kata Basic Python -  Ejercicio 8

"""
Pedir al usuario su peso (en kg) y estatura 
(en metros) para calcular el índice de masa corporal
y lo almacene en una variable, en imprima por pantalla
"""

peso = float(input("Introduzca su peso: "))
altura = float(input("Introduzca su altura: "))

imc = round(peso / (altura ** 2), 2)

print("Su IMC es de: ", imc)

