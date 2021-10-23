#Katas Basic Python - Ejercicio 5

#Fibonacci
def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):
        print(a)
        c = a + b
        a = b
        b = c
        


n =int(input("Por favor, introduzca duracion de la serie: "))
fibonacci(n)