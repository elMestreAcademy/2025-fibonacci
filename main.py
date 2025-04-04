def fibonacci_iterativo_termino(n: int) -> int:

    if n == 1:
        return 0

    if n == 2:
        return 1

    penultimo = 0
    ultimo = 1
    # no calculamos los 2 primeros terminos
    # por que ya están calculados (ultimo y penultimo)

    for i in range(n - 2):
        suma = ultimo + penultimo
        penultimo = ultimo
        ultimo = suma

    return suma


def fibonacci_recursivo_termino(n: int) -> int:
    if n == 1:
        return 0

    if n == 2:
        return 1

    return fibonacci_recursivo_termino(n-1) + fibonacci_recursivo_termino(n-2)


if __name__ == "__main__":

    n = 5
    if n <= 0:
        exit("Necesito que n sea un entero positivo")

    print(fibonacci_iterativo_termino(n))
    print(fibonacci_recursivo_termino(n))
