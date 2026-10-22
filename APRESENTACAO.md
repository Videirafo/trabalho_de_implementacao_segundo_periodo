9 algoritmos de ordenação

Trabalho de implementação — segundo período | 16/11/2026


1. apresentação

Nosso trabalho é sobre algoritmos de ordenação. Ordenar significa colocar números em uma sequência, normalmente do menor para o maior.

Por exemplo, se temos a lista [5, 2, 8, 1], o resultado esperado é [1, 2, 5, 8].

Fizemos nove algoritmos em Python. Todos chegam à lista ordenada, mas cada um usa um jeito diferente. O objetivo foi entender esses jeitos e comparar como funcionam.


1. Selection Sort — seleção

Ele procura o menor número da parte que ainda está bagunçada e coloca esse número na posição certa. Depois repete com o restante.

Exemplo: [4, 2, 3, 1] → [1, 2, 3, 4]. Primeiro encontra o 1 e troca com o 4.


Vantagem: simples de entender. Desvantagem: fica lento com muitos números.



2. Bubble Sort — bolha

Ele compara dois números que estão lado a lado. Se estiverem na ordem errada, troca. Faz isso várias vezes até terminar.

Exemplo: [4, 2, 1] → [2, 1, 4] → [1, 2, 4]. O maior vai para o final a cada rodada.

Vantagem: fácil de acompanhar. Desvantagem: faz muitas comparações.



3. Insertion Sort — inserção

É parecido com organizar cartas na mão: pego um número e coloco no lugar certo entre os que já organizei.

Exemplo: [5, 2, 4, 1] → [2, 5, 4, 1] → [2, 4, 5, 1] → [1, 2, 4, 5].

Vantagem: bom para listas pequenas. Desvantagem: pode ficar lento quando a lista está muito misturada.


4. Merge Sort — intercalação

Ele divide a lista em duas partes. Continua dividindo até sobrar um número em cada parte. Depois junta tudo, já colocando em ordem.

Exemplo: [4, 1, 3, 2] → [4, 1] e [3, 2] → [1, 4] e [2, 3] → [1, 2, 3, 4].

Vantagem: funciona bem com listas grandes. Desvantagem: cria listas extras na memória.



5. Quick Sort — ordenação rápida

Ele escolhe um número de referência, chamado pivô. Separa os menores, os iguais e os maiores. Depois faz o mesmo com as partes menores.

Exemplo: com pivô 3, os números [5, 1, 3, 2] ficam separados em [1, 2], [3] e [5]. Depois juntamos em ordem.

Vantagem: geralmente é rápido. Desvantagem: em alguns casos pode perder desempenho.



6. Heap Sort

Ele organiza os números para deixar o maior em destaque. Esse maior vai para o final da lista, e o processo se repete com os outros.

Exemplo: em [3, 1, 4, 2], o 4 é o maior e vai para a última posição; os demais são reorganizados.

Vantagem: mantém bom desempenho em listas grandes. Desvantagem: a organização interna é mais difícil de entender.



7. Counting Sort — contagem

Em vez de ficar comparando números, ele conta quantas vezes cada valor aparece. Depois monta a lista do menor para o maior.

Exemplo: [3, 1, 3, 2] tem um 1, um 2 e dois 3. Resultado: [1, 2, 3, 3].

Vantagem: rápido quando os valores estão em uma faixa pequena. Desvantagem: pode gastar muita memória se o maior valor for muito alto.



8. Radix Sort — dígitos

Ele ordena os números olhando uma casa de cada vez: unidades, depois dezenas, centenas e assim por diante.

Exemplo: em 21, 13 e 12, primeiro olha o último dígito; depois a casa das dezenas. No fim: [12, 13, 21].

Vantagem: bom para números inteiros. Desvantagem: precisa fazer várias passadas pelos dígitos.



9. Bucket Sort — grupos

Ele separa os números em grupos por faixa de valor. Ordena cada grupo e depois junta os grupos na sequência.

Exemplo: os números 2, 18, 4 e 12 podem ser separados em duas faixas: [2, 4] e [12, 18]. Depois ficam [2, 4, 12, 18].

Vantagem: pode ser rápido com números bem distribuídos. Desvantagem: pode ficar lento quando muitos números caem no mesmo grupo.

Detalhe do código: nossa versão usa o Insertion Sort para ordenar cada grupo.


Abra o terminal na pasta do projeto e rode:

bash
python testes.py
python main.py


Rodar:

- `testes.py` usa uma lista pequena para conferir se os nove algoritmos chegam à mesma ordem.
  
- `main.py` cria uma lista de 100.000 números aleatórios, de 0 a 9.999, e mostra o tempo de execução.
  
- Merge, Quick, Heap, Counting, Radix e Bucket recebem os 100.000 números no teste normal.
  
- Selection, Bubble e Insertion recebem 1.000 números, porque são mais lentos. Se o professor exigir testar os 100.000 nesses três também, altere `teste_completo = False` para `True` no `main.py`. **Isso pode demorar muito.
  
- Quando aparece `OK`, significa que o resultado bateu com a ordem correta.
- 

O programa gera os 100.000, mas usa a amostra de 1.000 para os três primeiros.



Possíveis Perguntas!

1. Por que existem nove algoritmos se todos fazem a mesma coisa?

Porque existem várias maneiras de resolver o mesmo problema. Algumas são mais simples de entender e outras funcionam melhor com muitos dados.


2. Por que os três primeiros usam só mil números?

Porque fazem muitas comparações e podem demorar demais com cem mil. Nós geramos os cem mil e deixamos uma opção para testar a lista completa, caso necessário.


3.O que o `random.randint(0, 9999)` faz?

Sorteia números entre 0 e 9.999. Pode repetir valores, e não tem problema.


4.O que é o `lista.copy()`?

Cria uma cópia da lista para a função ordenar sem mudar a original.


5.Por que aparece `sorted(lista)` no programa?

Só para conferir se o algoritmo acertou. A função `sorted` não é usada para implementar os nove algoritmos.


6.Por que o tempo muda de um computador para outro?

Porque depende do computador e do que ele está executando naquele momento.


7.O que significa a função chamar ela mesma?

É a chamada *recursão*. Merge e Quick repetem a mesma ideia em partes menores da lista. O Heap também chama sua função de ajuste quando precisa.


8.Funciona com números negativos?

A versão que fizemos foi testada com números inteiros de 0 a 9.999. Counting, Radix e Bucket desta atividade foram escritos para inteiros não negativos.


Ao testar, vimos que todos os algoritmos conseguem ordenar a lista. A diferença está na maneira como fazem isso e no tempo que podem gastar. Aprendemos que os métodos mais simples ajudam a entender a lógica, mas nem sempre são os melhores para listas grandes.

A principal conclusão é que a escolha do algoritmo depende do problema e dos dados que vamos ordenar.
