print("\nBienvenido a la Calculadora.")
print("Para salir, escribe Salir.")
print("Las operaciones son suma, multi, div, resta.\n")
n1 = input("Ingresa un número: ")

n1 = int(n1)

while True:
    op = input("Ingresa una operación: ")
    if op.lower() == "suma":

        n2 = input("Ingresa el siguiente número: ")

        n2 = int(n2)

        suma = n1 + n2
        mensaje = f"""La suma de los números {n1} y {n2}, es {suma}."""

        print(mensaje)

        n1 = suma

    elif op.lower() == "multi":

        n2 = input("Ingresa el siguiente número: ")

        n2 = int(n2)

        multi = n1 * n2
        mensaje = f"""La multiplicación de los números {n1} y {n2}, es {multi}."""

        print(mensaje)

        n1 = multi

    elif op.lower() == "div":

        n2 = input("Ingresa el siguiente número: ")

        n2 = int(n2)

        div = n1 / n2
        mensaje = f"""La división de los números {n1} y {n2}, es {div}."""

        print(mensaje)

        n1 = div

    elif op.lower() == "resta":

        n2 = input("Ingresa el siguiente número: ")

        n2 = int(n2)

        resta = n1 - n2
        mensaje = f"""La resta de los números {n1} y {n2}, es {resta}."""

        print(mensaje)

        n1 = resta

    elif op.capitalize() == "Salir":
        break
