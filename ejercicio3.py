import re

def palabras_minusculas(texto):
    patron = re.compile(r'\b[a-z]+\b')

    palabras_encontradas = patron.findall(texto.lower())

    return palabras_encontradas

texto_ejemplo = "Este es un Texto de EJEMPLO con varias palabras Minúsculas y Mayúsculas."

resultado = palabras_minusculas(texto_ejemplo)
print(resultado)
