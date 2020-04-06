"""
Debe crear un programa que logre replicar el siguiente patrón, donde el usuario ingrese un número, y ese
número corresponderá al número de filas que se debe generar. La soluciṕon debe estar dentro del
programa llamado genera_patron.py .
1
12
123
1234
12345
Considerar que el patrón debe comenzar por el número 1, y por ende, el último número de la última fila
corresponderá al número ingresado
"""

numero = int(input("ingrese un numero\n"))
contain=""
for i in range(1, numero + 1):
    for j in range(1,i + 1):
        contain+= str(j)
    contain += "\n"
print(contain)