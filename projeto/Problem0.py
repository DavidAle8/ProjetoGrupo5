

class LabirintoProblem(Problem):

    def __init__(self, map_grid, initial, goal):
        super().__init__(initial, goal)
        self.map_grid = map_grid
        self.m = len(map_grid)
        self.n = len(map_grid[0])
        

    def actions(self, state):
        
        x, y = state
        acts = []

        for action, (nx, ny) in {
            'DIR': (x, y+1),
            'ESQ': (x, y-1), 
            'CIMA': (x-1, y), 
            'BAIXO': (x+1, y)}.items():

            if 0 <= nx < self.m and 0 <= ny < self.n:
                if self.map_grid[nx][ny] != 1:
                    acts.append(action)

        return acts
    
    
    def result(self, state, action):
        
        x, y = state

        if action == 'DIR':
            return (x, y+1)
        elif action == 'ESQ':
            return (x, y-1)
        elif action == 'CIMA':
            return (x-1, y)
        elif action == 'BAIXO':
            return (x+1, y)
        
        
        
    def path_cost(self, custo_acumulado, state2):
        
        x, y = state2
        terreno = self.map_grid[x][y]
        
        return custo_acumulado + terreno

        
        
    def h(self, node):
        
        x1, y1 = node.state
        x2, y2 = self.goal
        
        # Estamos usando a distancia de Manhattan para h(n)
        return abs(x1 - x2) + abs(y1 - y2)


