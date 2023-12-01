import re

def es_codigo_empleado_valido(cadena):
    patron = re.compile(r'^EMP\d{3}$')

    if patron.match(cadena):
        return True
    else:
        return False

codigo1 = "EMP123"
codigo2 = "EMP456"
codigo3 = "EMP7890"

print(es_codigo_empleado_valido(codigo1))  
print(es_codigo_empleado_valido(codigo2))  
print(es_codigo_empleado_valido(codigo3))  
