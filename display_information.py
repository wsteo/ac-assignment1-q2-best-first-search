class displayInfo:
    
    @staticmethod
    def puzzleState(state):
        print("{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}".format(
            state[0][0],state[0][1],state[0][2],
            state[1][0],state[1][1],state[1][2],
            state[2][0],state[2][1],state[2][2]))

    @staticmethod
    def display_list(node_list,solution_path):
        for index in range(len(node_list)):
            displayInfo.puzzleState(node_list[index])
            if index < len(solution_path):
                print("Move: {}\n".format(solution_path[index]))
            else:
                print("Output\n")