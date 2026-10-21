import selection_sort
import bubble_sort
import insertion_sort
import merge_sort
import quick_sort
import heap_sort
import counting_sort
import radix_sort
import bucket_sort

lista = [5, 2, 8, 1, 5, 0]
esperado = [0, 1, 2, 5, 5, 8]

assert selection_sort.ordenar(lista) == esperado
assert bubble_sort.ordenar(lista) == esperado
assert insertion_sort.ordenar(lista) == esperado
assert merge_sort.ordenar(lista) == esperado
assert quick_sort.ordenar(lista) == esperado
assert heap_sort.ordenar(lista) == esperado
assert counting_sort.ordenar(lista) == esperado
assert radix_sort.ordenar(lista) == esperado
assert bucket_sort.ordenar(lista) == esperado

print('Os nove algoritmos passaram no teste.')
