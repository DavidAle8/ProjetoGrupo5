from aima.agents import Environment

class LabirintoEnvironment(Environment):
    
    def __init__(self, map_grid):
        super().__init__()
        self.map_grid = map_grid
        self.m = len(map_grid)
        self.n = len(map_grid[0])
    
    
    def execute_action(self, agent, action):
        
        x, y = agent.location

        # Para matrizes teremos que fazer desse jeito todas as direções, 
        # pois linha cresce para baixo e coluna cresce para direita:
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

    def render(self):
        # assume agente único
        agent = self.things[0]  
        ax, ay = agent.location

        print("-" * (self.n * 2))

        for i in range(self.m):
            row = []
            for j in range(self.n):

                if (i, j) == (ax, ay):
                    row.append("A")  # agente

                else:
                    cell = self.map_grid[i][j]

                    if cell == 1:
                        row.append("#")   # parede
                    elif cell == 0:
                        row.append(".")   # chão
                    else:
                        row.append(str(cell))  # custo

            print(" ".join(row))

        print()


