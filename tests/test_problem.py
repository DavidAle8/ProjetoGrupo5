import pytest
from problems.Problem0 import LabirintoProblem
from aima.search import astar_search, uniform_cost_search


# ---------- GOAL TEST ----------

def test_goal_test():
    grid = [
        [1, 1],
        [1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))

    assert problem.goal_test((1, 1)) is True
    assert problem.goal_test((0, 1)) is False


# ---------- ACTIONS ----------

def test_actions_nao_atravessa_parede():
    grid = [
        [1, 0],
        [1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))
    actions = problem.actions((0, 0))

    assert 'DIR' not in actions   # (0,1) é parede
    assert 'BAIXO' in actions     # (1,0) é válido


def test_actions_limites_matriz():
    grid = [
        [1, 1],
        [1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))
    actions = problem.actions((0, 0))

    assert 'CIMA' not in actions
    assert 'ESQ' not in actions


# ---------- PATH COST ----------

def test_path_cost_acumula_corretamente():
    grid = [
        [1, 3],
        [1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (0, 1))

    custo1 = problem.path_cost(0, (0, 0), 'DIR', (0, 1))
    assert custo1 == 3

    custo2 = problem.path_cost(custo1, (0, 1), 'ESQ', (0, 0))
    assert custo2 == 4


# ---------- HEURÍSTICA ----------

def test_heuristica_nunca_negativa():
    grid = [
        [1, 1],
        [1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))

    class Node:
        def __init__(self, state):
            self.state = state

    h_value = problem.h(Node((0, 0)))
    assert h_value >= 0


def test_heuristica_manhattan_correta():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (2, 2))

    class Node:
        def __init__(self, state):
            self.state = state

    h_value = problem.h(Node((0, 0)))
    assert h_value == 4   # |2-0| + |2-0|


# ---------- ARMADILHA HEURÍSTICA ----------

def test_armadilha_heuristica():
    grid = [
        [1, 9, 9, 9, 1],
        [1, 1, 1, 9, 1],
        [9, 9, 1, 9, 1],
        [1, 1, 1, 1, 1]
    ]

    problem = LabirintoProblem(grid, (0, 0), (0, 4))
    solution = astar_search(problem)

    # Caminho direto pela linha de cima seria caríssimo,
    # A* deve contornar por baixo
    assert solution.path_cost < 20


# ---------- EFICIÊNCIA: NÓS EXPANDIDOS ----------

def test_astar_expande_menos_que_ucs():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 9, 1],
        [9, 9, 1, 9, 1],
        [1, 1, 1, 1, 1]
    ]

    # Problema para UCS
    problem_ucs = LabirintoProblem(grid, (0, 0), (4, 4))
    sol_ucs = uniform_cost_search(problem_ucs)
    expanded_ucs = problem_ucs.expanded

    # Problema para A*
    problem_astar = LabirintoProblem(grid, (0, 0), (4, 4))
    sol_astar = astar_search(problem_astar)
    expanded_astar = problem_astar.expanded

    assert sol_ucs.path_cost == sol_astar.path_cost
    assert expanded_astar <= expanded_ucs