"""
Crear una variante del programa anterior llamado solo_pares_refactor.py . En este caso, el cero no
debe ser considerado (el cero no es par)
"""

numero = int(input("Ingrese un numero\n"))

for i in range(1,numero + 1):
    if i % 2 == 0:
        print(i)
