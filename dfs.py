from typing import List, Deque
from collections import deque
from time import time
from resource import getrusage, RUSAGE_SELF
from State import State
from utils import UP, DOWN, LEFT, RIGHT, DIRECTIONS, writeToFile

def dfs(root: State) -> None:
    start_time = time()

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
        currentState: State = fringe.pop()
        visited.append(currentState)

        if currentState.isGoal():
            end_time = time()

            while currentState.direction is not None:
                path_to_goal.appendleft(currentState.direction)
                currentState = currentState.parent
            cost_of_path = len(path_to_goal)
            path_to_goal = f'{path_to_goal}'.replace('deque(', '').replace(')', '')
            nodes_expanded = len(visited) - 1
            for state in fringe:
                if state.depth > search_depth:
                    search_depth = state.depth
            max_search_depth = search_depth
            for state in visited:
                if state.depth > max_search_depth:
                    max_search_depth = state.depth
            running_time = end_time - start_time
            max_ram_usage = getrusage(RUSAGE_SELF).ru_maxrss/1024
            writeToFile(path_to_goal, cost_of_path, nodes_expanded, search_depth, max_search_depth, running_time, max_ram_usage)
            return
        
        for childState in currentState.getChildrenReverse():
            if (childState is not None) and (childState not in fringe) and (childState not in visited):
                fringe.append(childState)
