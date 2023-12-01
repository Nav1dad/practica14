import re

def contiene_fecha_valida(cadena):
    patron = re.compile(r'\b\d{2}/\d{2}/\d{4}\b')

    resultado = patron.search(cadena)

    return resultado is not None

cadena1 = "La fecha es 28/11/2023."
cadena2 = "No hay fechas aquí."

print(contiene_fecha_valida(cadena1))  
print(contiene_fecha_valida(cadena2))  
