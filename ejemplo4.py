import re

def encontrar_ocurrencias(texto, palabra):
    patron = re.compile(fr'\b{re.escape(palabra)}\b', re.IGNORECASE)

    coincidencias = patron.finditer(texto)

    ubicaciones = [coincidencia.span() for coincidencia in coincidencias]

    return ubicaciones

texto_ejemplo = "Este es un ejemplo de una palabra específica. La palabra específica es específica."

palabra_a_buscar = "específica"

resultado = encontrar_ocurrencias(texto_ejemplo, palabra_a_buscar)
print(resultado)
