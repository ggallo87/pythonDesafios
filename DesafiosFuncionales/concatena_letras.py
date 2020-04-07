"""
Crear una función llamada gen que reciba el número de letras a generar, y devuelva un string con
todas las letras generadas concatendas.
Ejemplo:
gen 4
"abcd"
gen 10
"abcdefghij"
"""

import sys
import string

numero = int(sys.argv[1])


def gen(x):
    letras = string.ascii_letters
    contar = 0
    concatenar = ""
    while contar < numero:
        concatenar += letras[contar]
        contar += 1
    
    return str(concatenar)

print(str(gen(numero)))
