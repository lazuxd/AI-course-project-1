from typing import List, Deque
from collections import deque
from State import State
from utils import UP, DOWN, LEFT, RIGHT, DIRECTIONS, writeToFile

def bfs(root: State) -> None:
    path_to_goal: Deque[str] = deque()
    cost_of_path: int = 0
    nodes_expanded: int = 0
    search_depth: int = 0
    max_search_depth: int = 0
    running_time: float = 0
    max_ram_usage: float = 0

    fringe: Deque[State] = deque([root])
    visited: List[State] = []

    while len(fringe) > 0:
        currentState: State = fringe.popleft()
        visited.append(currentState)

        if currentState.isGoal():
            while currentState.direction is not None:
                path_to_goal.appendleft(currentState.direction)
                currentState = currentState.parent
            writeToFile(path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth, running_time, max_ram_usage)
            return
        
        for childState in currentState.getChildren():
            if (childState is not None) and (childState not in visited):
                fringe.append(childState)
        

    