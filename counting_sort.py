# Vantagem: rápido quando os números são pequenos.
# Desvantagem: gasta memória se o maior número for grande.
def ordenar(lista):
    if len(lista) == 0:
        return []
    contagem = [0] * (max(lista) + 1)
    for numero in lista:
        contagem[numero] = contagem[numero] + 1
    resultado = []
    for numero in range(len(contagem)):
        for i in range(contagem[numero]):
            resultado.append(numero)
    return resultado
