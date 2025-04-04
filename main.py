print("Fibonacci")

n = 10
penultimo = 0
ultimo = 1

if n < 3:
    exit("Necesito que n sea igual o superior a 3")

for i in range(2, n):
    suma = ultimo + penultimo
    penultimo = ultimo
    ultimo = suma

print(suma)
