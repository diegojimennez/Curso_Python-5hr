def sin_espacios(texto):
    for _ in texto:
        texto.replace(" ", "")
    return texto.replace(" ", "")


def reverse(texto):
    for _ in sin_espacios(texto):
        texto.capitalize()
    return texto.capitalize()


print("Hola Mundo")

se = sin_espacios("Aprende Python ahora! curso completo e intensivo desde cero")
rev = reverse(se)

print(se)
print(rev)
