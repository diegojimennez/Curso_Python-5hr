numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

primero, *otros = numeros
print(primero, otros)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penu, ultimo = numeros
print(segundo, penu, otros)
