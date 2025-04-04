def fibonacci_iterativo_termino(n: int) -> int:
    if n < 3:
        exit("Necesito que n sea igual o superior a 3")

    penultimo = 0
    ultimo = 1

    # no calculamos los 2 primeros terminos
    # por que ya están calculados (ultimo y penultimo)

    for i in range(n - 2):
        suma = ultimo + penultimo
        penultimo = ultimo
        ultimo = suma

    return suma


if __name__ == "__main__":
    print(fibonacci_iterativo_termino(5))
