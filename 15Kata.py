#Kata Basic Python

""""
Ejercicio 15
Crea una funcion llamada menorque() que nos devuelve 
en pantalla el numero menor entre dos enteros
"""

def menorque(num1,num2):
    
    if num1 == num2:
        return -1
    elif num1 < num2:
        return num1
    else:
        return num2

print(menorque(3,4))

