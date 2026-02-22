from aima.search import astar_search, uniform_cost_search
from problems.Problem0 import LabirintoProblem

def test_sem_solucao():
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    problem = LabirintoProblem(grid, (0,0), (2,2))

    solution = astar_search(problem)

    assert solution is None


def test_heuristica_admissivel():
    grid = [
        [0, 0, 0],
        [0, 5, 0],
        [0, 0, 0]
    ]

    problem = LabirintoProblem(grid, (0,0), (2,2))

    sol_ucs = uniform_cost_search(problem)
    sol_astar = astar_search(problem)

    assert sol_ucs.path_cost == sol_astar.path_cost


def test_escolha_otima():
    grid = [
        [0, 7, 0],
        [0, 7, 0],
        [0, 0, 0]
    ]

    problem = LabirintoProblem(grid, (0,0), (0,2))
    solution = astar_search(problem)

    assert solution.path_cost == 6


def test_multiplos_caminhos_otimos():
    grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    problem = LabirintoProblem(grid, (0,0), (2,2))
    solution = astar_search(problem)

    assert solution.path_cost == 4