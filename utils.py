from typing import List

UP = 'Up'
DOWN = 'Down'
LEFT = 'Left'
RIGHT = 'Right'

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def writeToFile(path_to_goal: List[str], cost_of_path: int, nodes_expanded: int, search_depth: int,
                max_search_depth: int, running_time: float, max_ram_usage: float) -> None:
    print(path_to_goal)
