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