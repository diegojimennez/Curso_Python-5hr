usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


# --FORMA NO TAN ELEGANTE--
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# --FORMA SENCILLA Y ELEGANTE-- transformacion
# map
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)


# filtrar
# filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)


# filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# Otra manera de escribir --map--
# nombres = list(map(lambda usuario: usuario[0], usuarios))
# print(nombres)

# Otra manera de escribir --filter--
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
