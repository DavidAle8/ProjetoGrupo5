from env.Environment0 import LabirintoEnvironment
from agents.Program0 import LabirintoAgentProgram
from aima.agents import Agent
from aima.search import greedy_best_first_search, uniform_cost_search, astar_search
import numpy as np


mapa = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

m = len(mapa)
n = len(mapa[0])

pos_inicial = (0,0)
pos_objetivo = (m-1,n-1)


algoritmos = {
    "A*": astar_search,
    "Uniform Cost": uniform_cost_search,
    "Greedy": greedy_best_first_search
}

def execucao_labirinto():
    
    for algoritmo in algoritmos.items():
        
        ambiente = LabirintoEnvironment(mapa)
        program = LabirintoAgentProgram(grid=mapa, goal=pos_objetivo, search_algorithm=algoritmo, initial_state=pos_inicial)
        agente = Agent(program)
        ambiente.add_thing(agente, location=pos_inicial)

        while not ambiente.is_done():
            ambiente.step()

        print("Local final:", agente.location)
        print("Performance:", agente.performance)
        
        
        
execucao_labirinto()