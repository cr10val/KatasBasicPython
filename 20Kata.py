#Kata Basic Python

"""
Crear la funcion del tipo abstracto PILA

pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)

print(pila.pop())
print(pila)
"""

class Pila:
    """Representa una pila con operaciones de apilar,
     desapilar y verificar si está vacia."""

    def __init__(self) -> None:
         """Crea una pila vacia."""
         #La pila vacia se representa con una lista vacia
         self.items=[]

    def apilar(self,x):
        """Agrega el elemento x a la pila"""
        self.append(x)

    def desapilar(self):
        """Saca el ultimo elemento de la pila"""
        try:
            return self.pop()
        except IndexError:
            raise ValueError("La pila está vacía")


    def vacia(self):
        """Devuelve true si esta vacia y false si no"""
        return self.items == []




p = Pila

p.apilar("1")
p.apilar(4)
p.apilar(9)

print(p)

p.desapilar()
print(p)