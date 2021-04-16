from queue import PriorityQueue
from puzzle import Puzzle
from display_information import displayInfo

def best_first_search(initial_state):
        count = 0
        explored = []
        start_node = Puzzle(initial_state, None, None, 0)
        opened = PriorityQueue()
        opened.put((start_node.heuristic_function,count,start_node))
        while not opened.empty():
            node = opened.get()
            node = node[2]
            explored.append(node.state)
            if node.is_goal():
                solution_path = node.find_solution()
                displayInfo.display_list(explored,solution_path)
                return solution_path

            children = node.generate_child()
            for child in children:
                if child.state not in explored:
                    count += 1
                    opened.put((child.heuristic_function,count,child))
        return