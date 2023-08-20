#Ejercicio 3
"""Implementar la clase pila vista en clase
"""
class Pila:
    """ Pila es una clase que implemente el tipo abstracto de datos 'pila' del tipo LIFO"""
    """definimos la pila vacia como la lista vacia"""
    def __init__(self):
        self.items = []

    def es_vacia(self)->bool:
        """pregunta si no hay niongun dato en la pila"""

    def incluir(self, item)->None:
        """agrega un elemento a mi pila"""

    def extraer(self):
        """extrae un elemento de la pila, en este caso el último de la lista"""

    def inspeccionar(self):
        """Ver cual es el tope de la pila"""

    def tamano(self):
        """me dice al cantidad de elementos que tenemos en la pila"""

    def __eq__(self,otra_pila)->bool:
        """Definimos cuando dos pilas son iguales"""

p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
print(p.items)
assert p.inspeccionar() == 1
assert p.items == [4, 2, 1]
#assert p.extraer() == 1
#assert p.inspeccionar() == 2
#print (p.inspeccionar())
print(p.items)

#Ejercicio 4 *
""" Modificar el init para que la pila pueda empezar con una lista
"""

pila = Pila([1,2,3,4])
previo = pila.extraer()
print(previo) # 4
assert previo == 4

#Ejercicio 5
""" Agregar a la clase Pila un método:
    - Vaciar pila.
"""
"""""
c. Vaciar pila.

p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
assert p.es_vacia() == False
p.vaciar_pila()
assert p.es_vacia() == True

"""