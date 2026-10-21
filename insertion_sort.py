# Vantagem: bom para listas pequenas.
# Desvantagem: lento em listas muito misturadas.
def ordenar(lista):
    numeros = lista.copy()
    for i in range(1, len(numeros)):
        atual = numeros[i]
        j = i - 1
        while j >= 0 and numeros[j] > atual:
            numeros[j + 1] = numeros[j]
            j = j - 1
        numeros[j + 1] = atual
    return numeros
