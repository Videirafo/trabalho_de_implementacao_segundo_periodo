# Trabalho de implementação — segundo período

**Apresentação:** 16/11/2026

Neste trabalho, fizemos nove algoritmos de ordenação em Python. Cada um organiza uma lista de números de um jeito diferente.

## Roteiro para apresentar ao professor

Preparei uma explicação simples de cada um dos nove algoritmos, com exemplos pequenos, o que falar durante os testes e respostas a perguntas comuns.

**[Abrir o roteiro de apresentação](./APRESENTACAO.md)**

O roteiro é material de estudo: leia, teste os exemplos e explique com suas próprias palavras.

## Como executar

Abra a pasta no VS Code e execute no terminal:

```bash
python main.py
```

O programa cria uma lista com **100.000 números aleatórios** e mostra o tempo de cada algoritmo.

Selection, Bubble e Insertion usam **1.000 números** no teste normal, porque podem demorar muito com 100.000. Para usar os 100.000 também nesses três, mude `teste_completo = False` para `True` no `main.py`.

Para conferir os nove algoritmos com uma lista pequena:

```bash
python testes.py
```

## Vantagens e desvantagens

| Algoritmo | Vantagem | Desvantagem |
|---|---|---|
| Selection | Fácil de entender | Lento com muitos números |
| Bubble | Simples de acompanhar | Muitas comparações |
| Insertion | Bom para listas pequenas | Lento com listas grandes |
| Merge | Bom para listas grandes | Usa outras listas |
| Quick | Geralmente rápido | Pode ficar lento em certos casos |
| Heap | Bom desempenho | Mais complicado |
| Counting | Rápido com números pequenos | Pode gastar memória |
| Radix | Bom para inteiros | Ordena por dígitos |
| Bucket | Bom com dados distribuídos | Depende dos grupos |

**Observação:** Counting, Radix e Bucket foram feitos para números inteiros maiores ou iguais a zero.

## Vídeos para estudar (opcional)

Se quiser visualizar as trocas dos números, estão aqui as demonstrações:

[Selection](videos/selection_sort.mp4) · [Bubble](videos/bubble_sort.mp4) · [Insertion](videos/insertion_sort.mp4) · [Merge](videos/merge_sort.mp4) · [Quick](videos/quick_sort.mp4) · [Heap](videos/heap_sort.mp4) · [Counting](videos/counting_sort.mp4) · [Radix](videos/radix_sort.mp4) · [Bucket](videos/bucket_sort.mp4)

## Conclusão

Os nove algoritmos ordenaram os números. Alguns são fáceis de aprender, mas mais lentos; outros funcionam melhor com listas grandes. Isso ajuda a entender por que existem diferentes formas de ordenar dados.
