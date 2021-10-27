#Kata Basic python

"""
Ejercicio 18

Crear una funcion llamada sumatorioNumeros que 
reciba como parametro un numero  y retorne la suma
de todos sus digitos
"""

def sumatorioNumeros(num):

    num_str = str(num)
    sum = 0
    for i in num_str:
        sum += int(i)
    return sum

print(sumatorioNumeros(2684))
