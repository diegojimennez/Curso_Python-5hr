# las TUPLAS son lo mismo que una LISTA, pero la TUPLAS no se pueden modificar

# Concatenar 2 TUPLAS
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Crear un LISTADO a una TUPLA
punto = tuple([1, 2])
print(punto)

# Acceder a los elementos de la TUPLA
menosNumeros = numeros[:2]
print(menosNumeros)

# Desempaquetar las TUPLAS
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Iterar las TUPLAS
for n in numeros:
    print(n)

# Modificar una TUPLA haciendola una LISTA (NO SE MODIFICA LA TUPLA, SE CREA UNA LISTA PARA PODER MODIFICAR ESTA LISTA)
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)
