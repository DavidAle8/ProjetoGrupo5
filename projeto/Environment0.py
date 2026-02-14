import sys
import os

from agents import Environment

class LabirintoEnvironment(Environment):
    
    def __init__(self, map_grid):
        super().__init__()
        self.map_grid = map_grid
        self.m = len(map_grid)
        self.n = len(map_grid[0])
        # self.initial = initial
        # self.goal = goal
    
    
    def execute_action(self, agent, action):
        
        x, y = agent.location

        # Em matrizes:
        #     linha cresce para baixo
        #     coluna cresce para direita
        #     CIMA    → (x-1, y)
        #     BAIXO   → (x+1, y)
        #     ESQ     → (x, y-1)
        #     DIR     → (x, y+1)

        if action == 'DIR':
            nx, ny = x, y+1
        elif action == 'ESQ':
            nx, ny = x, y-1
        elif action == 'CIMA':    
            nx, ny = x-1, y
        elif action == 'BAIXO':
            nx, ny = x+1, y
        else:
            return

        if 0 <= nx < self.m and 0 <= ny < self.n:
            if self.map_grid[nx][ny] != 1:
                agent.location = (nx, ny)

              
    def percept(self, agent):
        return agent.location
