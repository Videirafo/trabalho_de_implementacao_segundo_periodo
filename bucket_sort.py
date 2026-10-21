# Vantagem: rápido se os números estão bem distribuídos.
# Desvantagem: pode ser lento se ficarem no mesmo grupo.
import insertion_sort


def ordenar(lista):
    if len(lista) == 0:
        return []
    quantidade = min(len(lista), 1000)
    faixa = max(lista) // quantidade + 1
    baldes = []
    for i in range(quantidade):
        baldes.append([])
    for numero in lista:
        posicao = numero // faixa
        baldes[posicao].append(numero)
    resultado = []
    for balde in baldes:
        ordenados = insertion_sort.ordenar(balde)
        for numero in ordenados:
            resultado.append(numero)
    return resultado
