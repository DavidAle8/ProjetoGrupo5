from agents import Agent
from search import astar_search
from problems.Problem0 import LabirintoProblem


def labirinto_program(goal, grid):

    plan = []

    def program(percept):
        nonlocal plan

        if not plan:
            problem = LabirintoProblem(grid, percept, goal)
            solution = astar_search(problem)

            if solution is None:
                return None

            plan = solution.solution()

        if plan:
            return plan.pop(0)
        else:
            return None

    return program


