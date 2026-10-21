# Vantagem: fácil de acompanhar.
# Desvantagem: faz muitas comparações.
def ordenar(lista):
    numeros = lista.copy()
    for i in range(len(numeros)):
        for j in range(len(numeros) - 1 - i):
            if numeros[j] > numeros[j + 1]:
                auxiliar = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = auxiliar
    return numeros
