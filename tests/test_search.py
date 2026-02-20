from aima.search import astar_search, uniform_cost_search
from problems.Problem0 import LabirintoProblem


# ---------- CASO SEM SOLUÇÃO ----------

def test_sem_solucao():
    grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]

    problem = LabirintoProblem(grid, (0,0), (2,2))

    solution = astar_search(problem)

    assert solution is None


# ---------- HEURÍSTICA ADMISSÍVEL ----------

def test_heuristica_admissivel():
    grid = [
        [1, 1, 1],
        [1, 5, 1],
        [1, 1, 1]
    ]

    problem = LabirintoProblem(grid, (0,0), (2,2))

    sol_ucs = uniform_cost_search(problem)
    sol_astar = astar_search(problem)

    assert sol_ucs.path_cost == sol_astar.path_cost


# ---------- ESCOLHA ÓTIMA ----------

def test_escolha_otima():
    grid = [
        [1, 7, 1],
        [1, 7, 1],
        [1, 1, 1]
    ]

    problem = LabirintoProblem(grid, (0,0), (0,2))

    solution = astar_search(problem)

    # Caminho ótimo evita as células 7
    assert solution.path_cost == 4

# ---------- MÚLTIPLOS CAMINHOS ÓTIMOS ----------

def test_multiplos_caminhos_otimos():
    grid = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]

    problem = LabirintoProblem(grid, (0,0), (2,2))
    solution = astar_search(problem)

    # Existem vários caminhos ótimos
    assert solution.path_cost == 4