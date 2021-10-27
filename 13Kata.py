#Katas Basic Python

"""
Ejercicio 13
Crear una lista de numeros entereos y devuelva dos 
listas ordenadas. La primera con los numeros pares
y la segunda con los impares
"""
from typing import ParamSpec


def separar(a):
    a.sort()
    pares =[]
    impares=[]
    for i in a:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares


lista = [8,19,20,43,62,7,13,25,48,]

print(separar(lista))
