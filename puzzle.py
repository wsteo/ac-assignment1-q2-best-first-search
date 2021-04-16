from copy import deepcopy

class Puzzle:
    goal_state = [
        [1,2,3],
        [8,0,4],
        [7,6,5]
    ]
    heuristic_function = None
    num_of_instances = 0

    def __init__(self, state, parent, move, path_cost):
        self.parent = parent
        self.state = state
        self.move = move
        self.generate_heuristic()
        self.heuristic_function = self.heuristic
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        Puzzle.num_of_instances += 1
    
    def __str__(self):
        return str(self.state[0])+'\n'+str(self.state[1])+'\n'+str(self.state[2])

    # Calculate the heuristic for h(n). Comparing the incorrect tile
    def generate_heuristic(self):
        result = 0
        count = 1
        self.heuristic=0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal_state[i][j]:
                    result += 1
                count += 1
        self.heuristic = result

    def is_goal(self):
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_valid_moves(i,j):
        valid_moves = ['U','D','L','R']
        if i == 2:
            valid_moves.remove('U')
        elif i == 0:
            valid_moves.remove('D')
        if j == 2:
            valid_moves.remove('L')
        elif j == 0:
            valid_moves.remove('R')
        return valid_moves

    def generate_child(self):
        children=[]
        valid_moves=[]
        x = 0
        y = 0

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    x = i
                    y = j
                    valid_moves = self.find_valid_moves(i,j)

        for move in valid_moves:
            new_state = deepcopy(self.state)
            if move == 'U':
                new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
            elif move == 'D':
                new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
            elif move == 'R':
                new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
            elif move == 'L':
                new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
            children.append(Puzzle(new_state,self,move,1))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.move)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.move)
        solution = solution[:-1]
        solution.reverse()
        return solution