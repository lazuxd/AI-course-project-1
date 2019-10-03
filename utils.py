from typing import List

UP = 'Up'
DOWN = 'Down'
LEFT = 'Left'
RIGHT = 'Right'

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def writeToFile(path_to_goal: str, cost_of_path: int, nodes_expanded: int, search_depth: int,
                max_search_depth: int, running_time: float, max_ram_usage: float) -> None:
    
    print(f'path_to_goal: {path_to_goal}')
    print(f'cost_of_path: {cost_of_path}')
    print(f'nodes_expanded: {nodes_expanded}')
    print(f'search_depth: {search_depth}')
    print(f'max_search_depth: {max_search_depth}')
    print(f'running_time: {running_time}')
    print(f'max_ram_usage: {max_ram_usage}')
