#Kata Basic Python - Ejercicio 2

def compra(importe):
    if importe > 100:
        importe -= importe *0.1
    
    print("El importe de la compra es: ",importe)

compra(200)