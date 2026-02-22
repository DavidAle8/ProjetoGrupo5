# Especificação Formal do Problema

## Labirinto Traiçoeiro

Esta seção apresenta a especificação formal do problema conforme o modelo clássico de problemas de busca descrito em *Artificial Intelligence: A Modern Approach* de Artificial Intelligence: A Modern Approach, e implementado no repositório aimacode/aima-python.

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
* `best_first_graph_search` (para busca gulosa)
* `astar_search`

O algoritmo é chamado dentro do Programa do Agente, conforme exigido pela arquitetura Ambiente – Agente – Programa de Agente.

---

## Conclusão

O problema do Labirinto Traiçoeiro foi formalmente modelado como um problema clássico de busca, com:

* Estados bem definidos
* Ações válidas restritas
* Função de transição determinística
* Objetivo claramente especificado
* Custo de caminho acumulativo

Cada elemento formal possui correspondência direta com métodos implementados na classe `LabirintoProblem`, garantindo alinhamento entre a modelagem teórica e a implementação prática.
