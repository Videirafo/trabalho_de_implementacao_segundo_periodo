# Vantagem: bom para ordenar números inteiros.
# Desvantagem: precisa separar os números por dígito.
def ordenar(lista):
    numeros = lista.copy()
    if len(numeros) == 0:
        return []
    casa = 1
    maior = max(numeros)
    while maior // casa > 0:
        baldes = []
        for i in range(10):
            baldes.append([])
        for numero in numeros:
            digito = (numero // casa) % 10
            baldes[digito].append(numero)
        numeros = []
        for balde in baldes:
            for numero in balde:
                numeros.append(numero)
        casa = casa * 10
    return numeros
