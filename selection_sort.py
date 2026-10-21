# Vantagem: fácil de entender.
# Desvantagem: lento em listas grandes.
def ordenar(lista):
    numeros = lista.copy()
    for i in range(len(numeros)):
        menor = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[menor]:
                menor = j
        auxiliar = numeros[i]
        numeros[i] = numeros[menor]
        numeros[menor] = auxiliar
    return numeros
