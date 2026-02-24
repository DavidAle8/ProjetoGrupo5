from aima.agents import Environment

class LabirintoEnvironment(Environment):
    
    def __init__(self, map_grid):
        super().__init__()
        self.map_grid = map_grid
        self.m = len(map_grid)
        self.n = len(map_grid[0])
        self.path_history = []
    
    
    def execute_action(self, agent, action):

        x, y = agent.location

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
                self.path_history.append((nx, ny))

                nome, custo = self.info_terreno(nx, ny)

                agent.performance -= custo

                print(f"Ação executada pelo agente: {action}")
                print(f"Posição atual: {agent.location}")
                print(f"Obstáculo atual do terreno: {nome}")
                print(f"Custo do obstáculo: {custo}")
                print(f"Custo total: {-agent.performance}")

                
    def percept(self, agent):
        return agent.location
    
    
    def is_done(self):
        for agent in self.agents:
            if hasattr(agent, "goal") and agent.location == agent.goal:
                return True
        return False
    

    def info_terreno(self, x, y):

        obstaculos = self.map_grid[x][y]

        terrenos = {
            0: ("chão", 1),
            3: ("pedra", 3),
            5: ("lama", 5),
            7: ("espinhos", 7)
        }

        if obstaculos in terrenos:
            return terrenos[obstaculos]
        else:
            return ("Célula não idenficada.", obstaculos)

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
                    elif cell == 3:
                        row.append("o")   # pedra
                    elif cell == 5:
                        row.append("~")   # lama
                    elif cell == 7:
                        row.append("*")   # espinho
                    else:
                        row.append(str(cell))  # custo

            print(" ".join(row))

        print()
