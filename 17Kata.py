#Kata Basic Python

"""
Ejercicio 17
Escribe un programa que permita al usuario introducir 
una frase y luego un caracter y muestre la frase
introducida, pero con todas las ocurrencias del 
caracter indicado por el usuario reemplazadas por 
"-".
"""

frase = input("Introduzca una frase: ")
car = input("Introduzca un caracter: ")


final = frase.replace(car,"-")

print(final)