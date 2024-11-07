numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


# Esta funcion es una forma de poder ordenar los datos de un lista, sin embargo, Al usarla tenemos que crear muchas funciones para usar .sort Asi que no es tan uena idea

# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena, reverse=True)
# print(usuarios)

usuarios.sort(key=lambda el: el[1])
print(usuarios)
