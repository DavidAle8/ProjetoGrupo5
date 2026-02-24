# Classificação Formal do Ambiente

## Labirinto Traiçoeiro

Esta seção classifica o ambiente do problema conforme os critérios definidos em *Artificial Intelligence: A Modern Approach* de Artificial Intelligence: A Modern Approach.

---

## 1. Determinístico ou Estocástico

### Classificação: **Determinístico**

Um ambiente é determinístico quando o próximo estado é completamente determinado pelo estado atual e pela ação executada.

No Labirinto Traiçoeiro:

* Se o agente executa a ação `DIR`, ele sempre vai para `(x, y+1)`, caso o movimento seja válido.
* Não há aleatoriedade.
* O mesmo estado e mesma ação sempre produzem o mesmo resultado.

---

## 2. Totalmente ou Parcialmente Observável

### Classificação: **Totalmente Observável**

Um ambiente é totalmente observável quando o agente tem acesso completo às informações relevantes do estado.

No problema:

* O agente conhece a matriz completa.
* Ele conhece sua própria posição.
* Ele conhece o estado objetivo.
* Não há informação oculta.

Logo, o estado do mundo é completamente conhecido.

Portanto, o ambiente é **totalmente observável**.

---

## 3. Estático ou Dinâmico

### Classificação: **Estático**

Um ambiente é estático quando ele não muda enquanto o agente está deliberando.

No Labirinto:

* A matriz não se altera.
* As paredes não se movem.
* Os custos das células não mudam.
* Não há eventos externos.

O mundo só muda quando o agente executa uma ação.

Portanto, o ambiente é **estático**.

---

## 4. Discreto ou Contínuo

### Classificação: **Discreto**

Um ambiente é discreto quando:

* O conjunto de estados é finito ou enumerável.
* As ações são discretas.
* O tempo evolui em passos bem definidos.

No problema:

* Estados são posições inteiras da matriz.
* Ações são quatro movimentos possíveis.
* O agente se move passo a passo.

Logo, o ambiente é **discreto**.

---

## 5. Agente Único ou Múltiplos Agentes

### Classificação: **Agente Único**

O problema envolve apenas:

* Um agente navegando no labirinto.
* Nenhum outro agente influencia o ambiente.
* Não há competição nem cooperação.

Portanto, trata-se de um ambiente de **agente único**.

---

# Resumo Final da Classificação

O ambiente do Labirinto Traiçoeiro é:

* Determinístico
* Totalmente observável
* Estático
* Discreto
* De agente único
