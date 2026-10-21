# Vantagem: tem bom desempenho em listas grandes.
# Desvantagem: é mais difícil de entender.
def ajustar(numeros, tamanho, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    if esquerda < tamanho and numeros[esquerda] > numeros[maior]:
        maior = esquerda
    if direita < tamanho and numeros[direita] > numeros[maior]:
        maior = direita
    if maior != i:
        numeros[i], numeros[maior] = numeros[maior], numeros[i]
        ajustar(numeros, tamanho, maior)


def ordenar(lista):
    numeros = lista.copy()
    tamanho = len(numeros)
    for i in range(tamanho // 2 - 1, -1, -1):
        ajustar(numeros, tamanho, i)
    for i in range(tamanho - 1, 0, -1):
        numeros[0], numeros[i] = numeros[i], numeros[0]
        ajustar(numeros, i, 0)
    return numeros
