from search import astar_search # esse é só um dos algoritmos, podem adicionar mais
from agents import Agent
from Problem0 import LabirintoProblem

class Agent:
    def __init__(self, goal, grid):
        self.goal = goal
        self.grid = grid
        self.state = None
        self.plan = []

    def __call__(self, percept):
        self.state = percept  # posição atual

        if not self.plan:
            problem = LabirintoProblem(self.grid, self.state, self.goal)

            solution = astar_search(problem)
            self.plan = solution.solution()

        if self.plan:
            return self.plan.pop(0)
        else:
            return None

########### Classe com o Programa do agente

'''Deixei aqui porque no documento fala apenas de uma classe para os agentes e programas'''

class AgentDoLabirinto(Agent):
    def __init__(self, program):
        super().__init__(program)
