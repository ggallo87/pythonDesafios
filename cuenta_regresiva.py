"""
Reemplaza la instrucción for por while dentro del programa llamado cuenta_regresiva.py .
La impresión debe ser la misma:
"""

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

i = 0
while i < cuenta_regresiva:
    tmp = cuenta_regresiva
    print("Iteracion {}".format(tmp - i))
    i += 1
