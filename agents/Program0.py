from aima.search import SimpleProblemSolvingAgentProgram
from problems.Problem0 import LabirintoProblem
from aima.search import astar_search


class LabirintoAgentProgram(SimpleProblemSolvingAgentProgram):

    def __init__(self, grid, goal, search_algorithm, initial_state=None):
        super().__init__(initial_state)
        self.grid = grid
        self.goal = goal
        self.search_algorithm = search_algorithm

    def update_state(self, state, percept):
        return percept

    def formulate_goal(self, state):
        return self.goal

    def formulate_problem(self, state, goal):
        return LabirintoProblem(self.grid, state, goal)

    def search(self, problem):
        solution = self.search_algorithm(problem)
        if solution:
            return solution.solution()
        return []













# def labirinto_program(goal, grid):

#     plan = []

#     def program(percept):
#         nonlocal plan

#         if not plan:
#             problem = LabirintoProblem(grid, percept, goal)
#             solution = astar_search(problem)

#             if solution is None:
#                 return None

#             plan = solution.solution()

#         if plan:
#             return plan.pop(0)
#         else:
#             return None

#     return program


