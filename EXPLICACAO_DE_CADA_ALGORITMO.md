# Entendendo os 9 algoritmos — um de cada vez

Material para estudar **o código simples** antes da apresentação de **16/11/2026**. A ideia é conseguir mostrar um exemplo pequeno, explicar o que o programa faz e dizer uma vantagem e uma desvantagem.

**Comece por aqui:** imagine a lista `[5, 2, 8, 1]`. Ordenar significa deixar `[1, 2, 5, 8]`. Os nove métodos fazem isso, só que de maneiras diferentes.

## 1. Selection Sort (seleção)

**A ideia:** procurar o menor número da parte que falta organizar e colocá-lo no começo dessa parte.

**Passo a passo com [4, 2, 3, 1]:**

1. Olho todos os números e encontro o menor: **1**.
2. Troco o **1** com o primeiro número, **4**. Agora temos `[1, 2, 3, 4]`.
3. Como o primeiro já está certo, passo para o segundo lugar e procuro o menor do restante.
4. Continuo até terminar.

**No nosso código:** `i` é a posição que estamos organizando, `menor` guarda onde está o menor número encontrado, e `j` percorre o restante da lista. A variável `auxiliar` ajuda a trocar dois valores.

**Vantagem:** lógica fácil de aprender. **Desvantagem:** mesmo quando há muitos números, ele continua procurando e comparando bastante.

**Como explicar ao professor:** “Eu escolho a posição, procuro o menor do restante e faço a troca. Depois repito para a próxima posição.”

[Abrir código](selection_sort.py) · [Ver vídeo](videos/selection_sort.mp4)

## 2. Bubble Sort (bolha)

**A ideia:** comparar dois números vizinhos. Se estiverem na ordem errada, trocar os dois.

**Passo a passo com [4, 2, 1]:**

1. Comparo 4 com 2. Como 4 é maior, troco: `[2, 4, 1]`.
2. Comparo 4 com 1. Troco: `[2, 1, 4]`.
3. Na rodada seguinte, comparo 2 com 1 e troco: `[1, 2, 4]`.
4. Pronto: o maior foi chegando ao final em cada rodada.

**No nosso código:** `j` indica o número que está sendo comparado com `j + 1`, seu vizinho. A condição `numeros[j] > numeros[j + 1]` significa “o da esquerda é maior?”. Se for, fazemos a troca usando `auxiliar`.

**Vantagem:** dá para enxergar cada troca facilmente. **Desvantagem:** pode fazer muitas comparações e ficar demorado.

**Como explicar:** “Vou comparando de dois em dois. Se o maior está antes do menor, eu inverto os dois. Repito as rodadas até ordenar.”

[Abrir código](bubble_sort.py) · [Ver vídeo](videos/bubble_sort.mp4)

## 3. Insertion Sort (inserção)

**A ideia:** parecido com organizar cartas na mão. Pegamos um número e encaixamos onde ele deveria estar entre os que já vimos.

**Passo a passo com [5, 2, 4, 1]:**

1. O 5 fica sozinho no começo.
2. Pego o 2. Ele é menor que 5, então fica antes: `[2, 5, 4, 1]`.
3. Pego o 4. Ele fica entre 2 e 5: `[2, 4, 5, 1]`.
4. Pego o 1. Ele vai para o começo: `[1, 2, 4, 5]`.

**No nosso código:** `atual` é o número que quero encaixar. A variável `j` anda para trás, verificando os valores anteriores. O `while` abre espaço até chegar à posição correta.

**Vantagem:** costuma ser bom com poucos números ou uma lista quase pronta. **Desvantagem:** pode precisar deslocar vários valores quando a lista está muito misturada.

**Como explicar:** “Eu vou montando uma parte organizada e coloco cada novo número no espaço certo.”

[Abrir código](insertion_sort.py) · [Ver vídeo](videos/insertion_sort.mp4)

## 4. Merge Sort (intercalação)

**A ideia:** dividir a lista em partes pequenas e depois juntar essas partes, comparando os números para manter a ordem.

**Passo a passo com [4, 1, 3, 2]:**

1. Divido em `[4, 1]` e `[3, 2]`.
2. Continuo dividindo até ter apenas um número em cada parte.
3. Junto a primeira parte em ordem: `[1, 4]`. Faço o mesmo com a segunda: `[2, 3]`.
4. Junto as duas partes comparando os primeiros números de cada uma: `[1, 2, 3, 4]`.

**No nosso código:** `meio` marca onde dividir. `esquerda` e `direita` são as partes. `i` e `j` apontam os próximos números a comparar. `resultado.append(...)` coloca cada número na nova lista.

Quando `ordenar` chama `ordenar` novamente, chamamos isso de **recursão**: a mesma função trabalha com partes menores do problema.

**Vantagem:** bom desempenho em listas grandes. **Desvantagem:** cria listas extras para dividir e juntar.

**Como explicar:** “Primeiro eu divido, depois junto comparando os menores de cada parte.”

[Abrir código](merge_sort.py) · [Ver vídeo](videos/merge_sort.mp4)

## 5. Quick Sort (rápida)

**A ideia:** escolher um número de referência, chamado **pivô**, e separar os menores, iguais e maiores que ele.

**Passo a passo com [5, 1, 3, 2]:**

1. Nosso código escolhe o elemento do meio: **3**.
2. Os menores ficam no grupo `[1, 2]`.
3. O igual fica no grupo `[3]`, e o maior no grupo `[5]`.
4. Ordeno os grupos menores e maiores e junto: `[1, 2, 3, 5]`.

**No nosso código:** `pivo` guarda o número de referência. As listas `menores`, `iguais` e `maiores` recebem os valores conforme o `if`, `elif` e `else`. A função depois organiza os grupos menores e maiores.

**Vantagem:** geralmente é rápido. **Desvantagem:** dependendo de como os dados ficam divididos, pode trabalhar mais do que o esperado.

**Como explicar:** “Escolho um pivô, separo os números em três grupos e repito a ideia nas partes que faltam organizar.”

[Abrir código](quick_sort.py) · [Ver vídeo](videos/quick_sort.mp4)

## 6. Heap Sort

**A ideia:** organizar os valores em uma estrutura na qual o maior fica no começo. Depois, mandar esse maior para o fim e reorganizar o restante.

**Passo a passo com [3, 1, 4, 2]:**

1. Reorganizo os valores para o maior, **4**, ficar no começo: `[4, 2, 3, 1]`.
2. Troco o primeiro com o último. O **4** fica no final, onde deve permanecer.
3. Reorganizo apenas os números que sobraram.
4. Repito até terminar em `[1, 2, 3, 4]`.

**No nosso código:** a função `ajustar` verifica um número e duas posições ligadas a ele, chamadas `esquerda` e `direita`. Ela coloca o maior acima. A função `ordenar` repete esse ajuste e move os maiores para o fim.

Esse grupo de posições é chamado de **heap**. Não é necessário desenhar uma árvore inteira para explicar a ideia principal.

**Vantagem:** desempenho consistente em listas grandes. **Desvantagem:** sua organização interna é menos intuitiva que Bubble ou Selection.

**Como explicar:** “Eu faço o maior ficar em primeiro, passo ele para o final e faço de novo com os valores que sobraram.”

[Abrir código](heap_sort.py) · [Ver vídeo](videos/heap_sort.mp4)

## 7. Counting Sort (contagem)

**A ideia:** contar quantas vezes cada número aparece e reconstruir a lista na sequência correta.

**Passo a passo com [3, 1, 3, 2]:**

1. Conto os valores: o **1** aparece uma vez; o **2**, uma vez; o **3**, duas vezes.
2. Escrevo os números começando pelo menor, repetindo cada um pela quantidade contada.
3. Resultado: `[1, 2, 3, 3]`.

**No nosso código:** `contagem` é uma lista de quantidades. Cada vez que encontro `numero`, faço `contagem[numero] = contagem[numero] + 1`. Depois, com dois `for`, coloco os valores em `resultado`.

**Vantagem:** pode ser muito rápido se a faixa de valores é pequena. **Desvantagem:** se o maior número for enorme, a lista de contagem pode ocupar muita memória.

**Como explicar:** “Em vez de trocar posições, eu conto os valores e monto outra lista já ordenada.”

[Abrir código](counting_sort.py) · [Ver vídeo](videos/counting_sort.mp4)

## 8. Radix Sort (por dígitos)

**A ideia:** ordenar olhando uma casa decimal por vez: unidades, dezenas, centenas e assim por diante.

**Passo a passo com [21, 13, 12]:**

1. Pelas **unidades**: 21 termina em 1, 12 em 2 e 13 em 3. Fica `[21, 12, 13]`.
2. Pelas **dezenas**, mantendo a ordem anterior dos que têm a mesma dezena: fica `[12, 13, 21]`.
3. Não há outras casas relevantes. A lista está ordenada.

**No nosso código:** `casa` começa em 1 (unidade), passa para 10 (dezena) e depois 100. A expressão `(numero // casa) % 10` descobre o dígito da casa que estamos olhando. Os `baldes` guardam os números de cada dígito de 0 a 9.

**Vantagem:** bom para muitos números inteiros. **Desvantagem:** precisa fazer uma rodada para cada casa decimal.

**Como explicar:** “Eu não comparo o número inteiro logo de cara: primeiro ordeno pelas unidades, depois dezenas, até acabar os dígitos.”

[Abrir código](radix_sort.py) · [Ver vídeo](videos/radix_sort.mp4)

## 9. Bucket Sort (grupos)

**A ideia:** dividir os números em grupos conforme a faixa de valor, ordenar os grupos e juntar tudo no final.

**Passo a passo com [2, 18, 4, 12]:**

1. Nosso código, com esses quatro números, cria **quatro grupos** de faixas de 5 em 5.
2. O grupo de 0 a 4 recebe `[2, 4]`; o de 5 a 9 fica vazio; o de 10 a 14 recebe `[12]`; e o de 15 a 19 recebe `[18]`.
3. Ordeno os valores dentro de cada grupo.
4. Junto os grupos em sequência: `[2, 4, 12, 18]`.

**No nosso código:** `quantidade` define quantos baldes teremos, `faixa` define os intervalos e `posicao` escolhe o grupo de cada número. Para ordenar cada grupo, este código usa nosso próprio **Insertion Sort**.

**Vantagem:** pode ser rápido quando os valores estão bem distribuídos. **Desvantagem:** se muitos ficarem no mesmo grupo, a ordenação desse grupo pode ficar lenta.

**Como explicar:** “Primeiro separo os números por faixa. Organizo os números dentro de cada faixa e, por último, junto os grupos.”

[Abrir código](bucket_sort.py) · [Ver vídeo](videos/bucket_sort.mp4)

---

## O que explicar no `main.py`

- `import random`: usamos para sortear os números.
- `import time`: usamos para medir quanto tempo cada função levou.
- O `for` cria **100.000 valores aleatórios entre 0 e 9.999**.
- `testar(...)` executa uma função, mede o tempo e verifica se a lista ficou correta.
- `sorted(lista)` aparece **só na conferência**, para comparar o resultado. A implementação de cada algoritmo está no seu próprio arquivo.
- O programa usa **1.000 valores no Selection, Bubble e Insertion** no teste padrão, porque eles são muito lentos com 100.000. Os outros seis usam os 100.000. Para testar tudo com 100.000, altere `teste_completo` para `True`, sabendo que pode demorar bastante.
- No final de cada linha, `OK` significa que o algoritmo chegou ao resultado esperado.

## Três coisas para não confundir na apresentação

1. **Todos ordenam; o jeito de ordenar muda.** Bubble troca vizinhos, Selection procura o menor, Counting conta, Radix separa por dígitos, e assim por diante.
2. **Os tempos não são diretamente comparáveis se o tamanho da lista não é o mesmo.** Não diga que um método com 1.000 elementos foi mais rápido que outro com 100.000 em condições iguais.
3. **Nosso exercício usa números inteiros não negativos.** Não afirme que Counting, Radix e Bucket desta versão aceitam qualquer tipo de dado.

**Material complementar:** [roteiro para falar com o professor](APRESENTACAO.md). Você pode estudar primeiro este guia, depois usar o roteiro mais curto para treinar a apresentação.
