# SET significa GRUPO o CONJUNTO
# Definicion: es un conjunto de DATOS que NO SE PUEDE REPETIR y que TAMPOCO esta ORDENADA

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)
segundo = [3, 4, 5]
segundo = set(segundo)

# Union '|'
print(primer | segundo)

# Intersección '&'
print(primer & segundo)

# Diferencia '-' calcula la diferencia entre 2 SETS, quitando los elementos del primer SET
print(primer - segundo)

# Diferencia Simetrica '^' va a devolver los elementos que esten en el SET 1 y 2 pero que no se encuentren entre el 1 y 2
print(primer ^ segundo)

# ---PROBLEMAS DE LOS SETS---
# Los SETS no se encuentren ORDENADOS y no podemos acceder a un elemento de estos
# segundo[0] ---> ERROR ya que no se pueden acceder a los elementos de los SETS
# ---Posible SOLUCION---
if 5 in segundo:
    print("Hola Mundo")
