# Especificação Formal do Problema

## Labirinto Traiçoeiro

Esta seção apresenta a especificação formal do problema conforme o modelo clássico de problemas de busca descrito em *Artificial Intelligence: A Modern Approach* de Artificial Intelligence: A Modern Approach, e implementado no repositório aimacode/aima-python.

O problema consiste em colocar um agente em um ambiente de um labirinto com paredes em volta e alguns obstáculos no meio da trajetória. 

O mesmo deve escolher caminhos estratégicos para evitar ao máximo passar pelos obstáculos existentes no labirinto. 

Cada obstáculo possui uma certa dificuldade para ser enfrentada e ultrapassada que terão um custo baseado no valor de sua célula. 

O mapa possui:

* Chão: valor 0 na célula, custa 1 para atravessar
* Parede: valor 1 na célula, não é possível atravessar
* Pedra no caminho: valor 3 na célula, custa 3 para atravessar
* Lama no caminho: valor 5 na célula, custa 5 para atravessar
* Espinhos no caminho: valor 7 na célula, custa 7 para atravessar

O agente será colocado em um ponto de partida e terá que atravessar o labirinto escolhendo o melhor caminho (o menos custoso). 
Existirá várias formas de se chegar ao objetivo, algumas serão sub ótimas comparando as outras.

---

## 1. Representação dos Estados

### Definição Formal

Um estado é representado como um par ordenado:

s = (x, y)

onde:

* x representa a linha da matriz
* y representa a coluna da matriz

O estado descreve exclusivamente a posição atual do agente no labirinto.

O espaço de estados é composto por todas as posições válidas da matriz que não correspondem a paredes.

### Implementação no Código

Arquivo: `problems/Problem0.py`

Classe:

```python
class LabirintoProblem(Problem):
```

O estado é representado pelo parâmetro `state`, utilizado nos métodos:

* `actions(self, state)`
* `result(self, state, action)`
* `goal_test(self, state)`

---

## 2. Estado Inicial

### Definição Formal

O estado inicial é a posição inicial do agente no labirinto:

s0 = (x0, y0)

Esse valor é definido externamente e passado ao problema.

### Implementação no Código

No `main.py`:

```python
pos_inicial = (0, 0)
```

No construtor do problema:

```python
def __init__(self, grid, initial, goal):
    super().__init__(initial, goal)
```

O estado inicial é armazenado como `self.initial`.

---

## 3. Conjunto de Ações

### Definição Formal

Para um estado s = (x, y), as ações possíveis são:

A(s) = {CIMA, BAIXO, ESQ, DIR}

Uma ação é válida apenas se:

* A nova posição estiver dentro dos limites da matriz
* A célula de destino não for uma parede (valor 1)

### Implementação no Código

Método:

```python
def actions(self, state):
```

Neste método:

* São geradas as quatro possíveis direções
* São filtradas as ações que levariam o agente para fora da matriz
* São descartadas ações que levam a células com valor 1 (parede)

---

## 4. Modelo de Transição (result(s, a))

### Definição Formal

A função de transição define o novo estado após a execução de uma ação.

Exemplos:

result((x, y), DIR) = (x, y+1)
result((x, y), ESQ) = (x, y-1)
result((x, y), CIMA) = (x-1, y)
result((x, y), BAIXO) = (x+1, y)

### Implementação no Código

Método:

```python
def result(self, state, action):
```

Este método retorna a nova tupla (x, y) correspondente à ação escolhida.

---

## 5. Teste de Objetivo (goal_test)

### Definição Formal

O teste de objetivo verifica se o estado atual corresponde ao estado objetivo:

goal_test(s) = True se s == goal
goal_test(s) = False caso contrário

### Implementação no Código

Método:

```python
def goal_test(self, state):
    return state == self.goal
```

O estado objetivo é definido no `main.py`:

```python
pos_objetivo = (m-1, n-1)
```

---

## 6. Custo de Caminho (path_cost)

### Definição Formal

O custo total do caminho é a soma dos custos das células atravessadas.

Cada tipo de célula possui o seguinte custo:

* Chão (0) → custo 0
* Pedra (3) → custo 3
* Lama (5) → custo 5
* Espinhos (7) → custo 7
* Parede (1) → não é permitido atravessar

Formalmente:

path_cost = soma dos valores das células visitadas

### Implementação no Código

Método:

```python
def path_cost(self, c, state1, action, state2):
```

O custo é atualizado somando o valor da célula de destino ao custo acumulado anterior `c`.

---

## Observação sobre o Uso da Busca

O problema é resolvido utilizando algoritmos de busca implementados no repositório `aima-python`, como:

* `uniform_cost_search`
* `astar_search`
* `greedy_best_first_graph_search`
* `best_first_graph_search` (utilizado indiretamente pelos algoritmos acima)

O algoritmo é chamado dentro do Programa do Agente, conforme exigido pela arquitetura Ambiente – Agente – Programa de Agente.

---

# 7. Algoritmos de Busca e Heurísticas

Os algoritmos utilizados neste projeto foram selecionados a partir da classe `search` do repositório aimacode/aima-python, conforme o modelo clássico apresentado em Artificial Intelligence: A Modern Approach.

O problema modelado (Labirinto Traiçoeiro) é um problema clássico de busca em grafo com:

* espaço de estados discreto
* ambiente determinístico
* agente único
* possibilidade de custos variáveis por célula
* estado objetivo bem definido

---

## Algoritmos Utilizados

Foram utilizados os seguintes algoritmos:

* `uniform_cost_search`
* `astar_search`
* `greedy_best_first_graph_search`
* `best_first_graph_search` (utilizado indiretamente pelos algoritmos acima)

### Justificativa

### Uniform Cost Search

Adequado para problemas com custos variáveis.
Garante encontrar a solução de menor custo acumulado.

### A* Search

Utiliza custo acumulado somado a uma heurística admissível.
Garante solução ótima quando a heurística é admissível e consistente.
É mais eficiente que Uniform Cost Search na prática.

### Greedy Best-First Search

Utiliza apenas a heurística para guiar a busca.
Não garante solução ótima, mas permite comparação de desempenho.

### Best-First Graph Search

É a base estrutural utilizada por A* e Greedy, sendo usada indiretamente.

---

## Algoritmos Não Utilizados

Os seguintes algoritmos disponíveis na classe `search` não foram utilizados:

* `breadth_first_tree_search`
* `breadth_first_graph_search`
* `bidirectional_search`
* `depth_first_tree_search`
* `depth_first_graph_search`
* `depth_limited_search`
* `iterative_deepening_search`
* `recursive_best_first_search`
* `hill_climbing`
* `simulated_annealing_full`
* `and_or_graph_search`

---

## Justificativa para Não Utilização

### Breadth-First Search (BFS)

Encontra o caminho com menor número de passos, mas não considera custos diferentes nas células.
Como o problema envolve custos variáveis, BFS pode retornar soluções não ótimas.

---

### Depth-First Search (DFS)

Não garante solução ótima.
Pode explorar caminhos muito profundos e ineficientes antes de encontrar o objetivo.

---

### Depth-Limited Search e Iterative Deepening

Indicados quando a profundidade da solução é desconhecida e o custo é uniforme.
Não consideram custo acumulado, sendo inadequados para o problema com pesos diferentes.

---

### Bidirectional Search

Embora o algoritmo bidirectional_search esteja disponível no módulo search do repositório aimacode/aima-python, ele não foi utilizado na versão final do projeto, pois, diferentemente dos algoritmos:

* `astar_search`
* `uniform_cost_search`
* `greedy_best_first_graph_search`

O bidirectional_search da AIMA não retorna um objeto Node, mas sim o custo mínimo encontrado.

O programa de agente foi estruturado para trabalhar com o padrão:

```python
node = algoritmo(problem)
node.solution()
```

Como o bidirecional não retorna um Node, ele não é diretamente compatível com a arquitetura adotada.

---

### Recursive Best-First Search (RBFS)

É uma variação de A* com menor consumo de memória.
Não foi utilizado por simplicidade de implementação, uma vez que A* já atende adequadamente aos requisitos do problema.

---

### Hill Climbing e Simulated Annealing

São algoritmos de busca local.
Não garantem solução ótima.
Podem ficar presos em mínimos locais.
O problema exige busca ótima baseada em custo acumulado.

---

### AND-OR Graph Search

Indicado para problemas não determinísticos.
O Labirinto Traiçoeiro é determinístico, logo este algoritmo não se aplica.

---

## Conclusão

O problema do Labirinto Traiçoeiro foi formalmente modelado como um problema clássico de busca, com:

* Estados bem definidos
* Ações válidas restritas
* Função de transição determinística
* Objetivo claramente especificado
* Custo de caminho acumulativo

Foram selecionados algoritmos adequados a:

* ambientes determinísticos
* espaços de estados discretos
* problemas com custos variáveis
* necessidade de comparação entre estratégias

Cada elemento formal possui correspondência direta com métodos implementados na classe `LabirintoProblem`, garantindo alinhamento entre a modelagem teórica e a implementação prática.


