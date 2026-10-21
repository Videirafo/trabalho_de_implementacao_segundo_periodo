import random
import time
import selection_sort
import bubble_sort
import insertion_sort
import merge_sort
import quick_sort
import heap_sort
import counting_sort
import radix_sort
import bucket_sort

# Troque para True se quiser testar 100.000 em todos (pode demorar muito).
teste_completo = False

numeros = []
for i in range(100000):
    numeros.append(random.randint(0, 9999))

amostra = numeros[:1000]
if teste_completo:
    amostra = numeros


def testar(nome, funcao, lista):
    inicio = time.time()
    resultado = funcao(lista)
    segundos = round(time.time() - inicio, 3)
    if resultado == sorted(lista):
        print(nome, '-', len(lista), 'números -', segundos, 'segundos - OK')
    else:
        print(nome, '- ERRO')


print('Lista criada com 100.000 números aleatórios.\n')
testar('Selection Sort', selection_sort.ordenar, amostra)
testar('Bubble Sort', bubble_sort.ordenar, amostra)
testar('Insertion Sort', insertion_sort.ordenar, amostra)
testar('Merge Sort', merge_sort.ordenar, numeros)
testar('Quick Sort', quick_sort.ordenar, numeros)
testar('Heap Sort', heap_sort.ordenar, numeros)
testar('Counting Sort', counting_sort.ordenar, numeros)
testar('Radix Sort', radix_sort.ordenar, numeros)
testar('Bucket Sort', bucket_sort.ordenar, numeros)
