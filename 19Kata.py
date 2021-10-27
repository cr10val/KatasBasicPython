#Kata Basic Python

""""
Ejercicio 19

Escribir un programa que almacene las matrices A y B 
en una tupla y muestre por pantalla su producto
"""

a = ((2,3,4),(5,6,7))
b = ((1,2),(3,4),(5,6))

c=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for i in range(len(c)):
    c[i] = tuple(c[i])

c = tuple(c)

for i in range(len(c)):
    print(c[i])



