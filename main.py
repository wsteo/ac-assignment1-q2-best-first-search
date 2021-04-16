from solution import best_first_search
from puzzle import Puzzle
from display_information import displayInfo

initialState = [
    [2,8,3],
    [1,6,4],
    [7,0,5]
]
print("Starting State")
displayInfo.puzzleState(initialState)
print("")
Puzzle.num_of_instances = 0
bestFirstSearch = best_first_search(initialState)
print("Steps to solve the puzzle\n{}".format(bestFirstSearch))
print("Space: {}".format(Puzzle.num_of_instances))