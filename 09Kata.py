#Kata Basic Python - Ejercicio 9

"""
Escribir un programa que pregunte al usuario una 
catidad a invertir, el interés porcentual anual y el 
número de años, y mueste por pantalla el capital 
obtenido en la inversion redondeando con dos 
decimales
"""

inv = float(input("Cantidad a invertir: "))
interest =  float(input("Interés anual(%): "))
years = int(input("Durante cuantos años: "))

total = round(inv * (interest /100 + 1 ) ** years,2)

print("Capital total: ", total)



