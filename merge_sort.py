# Vantagem: funciona bem com listas grandes.
# Desvantagem: precisa criar outras listas.
def ordenar(lista):
    if len(lista) <= 1:
        return lista.copy()
    meio = len(lista) // 2
    esquerda = ordenar(lista[:meio])
    direita = ordenar(lista[meio:])
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i = i + 1
        else:
            resultado.append(direita[j])
            j = j + 1
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i = i + 1
    while j < len(direita):
        resultado.append(direita[j])
        j = j + 1
    return resultado
