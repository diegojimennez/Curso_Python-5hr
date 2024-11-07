# Los DICCIONARIOS son una conexión de datos que se encuentran agrupados por una LLAVE y un VALOR

punto = {"x": 25, "y": 50}
print(punto)

# Imprimir 1 LLAVE especifica
print(punto["x"])
print(punto["y"])

# Agregar 1 LLAVE nueva
punto["z"] = 45

# Buscar 1 LLAVE que no existe
# print(punto, punto["lala"]) ---> ERROR ya que no existe esta LLAVE
if "lala" in punto:
    print("encontre lala", punto["lala"])

# Método para acceder a un valor del DICCIONARIO, sin que la APP explote
print(punto.get("x"))
print(punto.get("lala", 97))

# Eliminar alguna LLAVE incluidos sus VALORES
del punto["x"]
# Funcion DEL para eliminar una LLAVE
del punto["y"]

print(punto)
# Agregar nuevamente la LLAVE y VALOR de X
punto["x"] = 25

# Iterar todas las LLAVES junto con su VALOR
for valor in punto:
    print(valor, punto[valor])

# Forma más conveniente
for valor in punto.items():
    print(valor)  # Imprime TUPLAS

for llave, valor in punto.items():
    print(llave, valor)  # Ya no imprime TUPLAs


# ---- USO REAL DE LOS DICCIONARIOS ----

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
