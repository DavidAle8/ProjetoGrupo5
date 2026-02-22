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

desenho = np.array([
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0], 
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 0], 
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0], 
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
])


mapa_1 = np.array([
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 7, 3, 0, 0, 0, 5, 0],
    [1, 0, 5, 0, 1, 1, 1, 3, 1, 3], 
    [1, 3, 1, 0, 0, 1, 0, 7, 1, 0],
    [1, 3, 1, 1, 3, 1, 0, 1, 1, 7], 
    [1, 0, 7, 1, 0, 1, 3, 1, 1, 7], 
    [1, 1, 1, 1, 5, 1, 3, 0, 1, 0], 
    [0, 0, 0, 7, 0, 1, 1, 3, 1, 5],
    [7, 1, 1, 1, 0, 1, 1, 0, 1, 7], 
    [1, 1, 1, 1, 1, 1, 1, 5, 0, 0]
])



m = len(mapa)
n = len(mapa[0])

pos_inicial = (0,0)
pos_objetivo = (m-1,n-1)


algoritmos = {
    "Greedy": greedy_best_first_search,
    "Uniform Cost": uniform_cost_search,
    "A*": astar_search
}


def execucao_labirinto():
    
    for busca, algoritmo in algoritmos.items():
        
        print(f"\n\n\t\t\t ************* Resultado da Execução do labirinto com {busca} ************* \n\n")
        
        ambiente = LabirintoEnvironment(mapa_1)
        program = LabirintoAgentProgram(
            grid=mapa_1, 
            goal=pos_objetivo, 
            search_algorithm=algoritmo, 
            initial_state=pos_inicial
        )
        
        agente = Agent(program)
        ambiente.add_thing(agente, location=pos_inicial)

        while not ambiente.is_done():
            ambiente.step()

        print("Local final:", agente.location)
        print("Performance:", agente.performance)
        print("Caminho percorrido:", ambiente.path_history)
        print("Total de passos do algoritmo até o objetivo: ", len(ambiente.path_history))
        print("\n\n")
      
        
        
execucao_labirinto()