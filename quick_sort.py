# Vantagem: geralmente é rápido.
# Desvantagem: pode ficar lento em alguns casos.
def ordenar(lista):
    if len(lista) <= 1:
        return lista.copy()
    pivo = lista[len(lista) // 2]
    menores = []
    iguais = []
    maiores = []
    for numero in lista:
        if numero < pivo:
            menores.append(numero)
        elif numero > pivo:
            maiores.append(numero)
        else:
            iguais.append(numero)
    return ordenar(menores) + iguais + ordenar(maiores)
