"""
Crear un programa llamado solo_pares.py , que muestre todos los números pares hasta "n"
(incluyendo "n", si éste es par), donde "n" es un valor ingresado por el usuario
"""

numero = int(input("Ingrese un numero\n"))

for i in range(numero + 1):
    if i % 2 == 0:
        print(i)
