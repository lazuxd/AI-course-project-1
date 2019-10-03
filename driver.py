from State import State
from bfs import bfs
from dfs import dfs
from ast import ast
import sys

if __name__ == '__main__':
    alg = sys.argv[1]
    lst = sys.argv[2].split(',')
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    func = None
    if alg == 'bfs':
        func = bfs
    elif alg == 'dfs':
        func = dfs
    else:
        func = ast
    
    func(State(lst, None, None, 0))
