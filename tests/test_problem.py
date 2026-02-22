import pytest
from problems.Problem0 import LabirintoProblem
from aima.search import astar_search

# testa se o estado do objetivo está correto
def test_goal_test():
    grid = [
        [0, 0],
        [0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))

    assert problem.goal_test((1, 1)) is True
    assert problem.goal_test((0, 1)) is False


def test_actions_nao_atravessa_parede():
    grid = [
        [0, 1],
        [0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))
    actions = problem.actions((0, 0))

    assert 'DIR' not in actions   # (0,1) é parede
    assert 'BAIXO' in actions     # (1,0) é válido


def test_actions_limites_matriz():
    grid = [
        [0, 0],
        [0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))
    actions = problem.actions((0, 0))

    assert 'CIMA' not in actions
    assert 'ESQ' not in actions


def test_path_cost_acumula_corretamente():
    grid = [
        [0, 5],
        [0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (0, 1))

    custo1 = problem.path_cost(0, (0, 0), 'DIR', (0, 1))
    assert custo1 == 5

    custo2 = problem.path_cost(custo1, (0, 1), 'ESQ', (0, 0))
    assert custo2 == 6   # soma 1 do chão


def test_heuristica_nunca_negativa():
    grid = [
        [0, 0],
        [0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (1, 1))

    class Node:
        def __init__(self, state):
            self.state = state

    h_value = problem.h(Node((0, 0)))
    assert h_value >= 0


def test_heuristica_manhattan_correta():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (2, 2))

    class Node:
        def __init__(self, state):
            self.state = state

    h_value = problem.h(Node((0, 0)))
    assert h_value == 4


# testa desvio de caminho caro
def test_armadilha_heuristica():
    grid = [
        [0, 9, 9, 9, 0],
        [0, 0, 0, 9, 0],
        [9, 9, 0, 9, 0],
        [0, 0, 0, 0, 0]
    ]

    problem = LabirintoProblem(grid, (0, 0), (0, 4))
    solution = astar_search(problem)

    assert solution.path_cost < 30