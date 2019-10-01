from typing import List
from utils import UP, DOWN, LEFT, RIGHT

class State:
    def __init__(self, vector: List[int], direction: str, parent: 'State', *args, **kwargs):
        if vector != None:
            self.vector = vector
        else:
            self.vector = [i for i in range(9)]
        self.direction = direction
        self.parent = parent
    
    def __str__(self):
        return self.toString()
    
    def __repr__(self):
        return self.toString()

    def __eq__(self, other: 'State'):
        return self.vector == other.vector
    
    def _getEmptyIndex(self) -> int:
        return self.vector.index(0)

    def toString(self) -> str:
        return '['+', '.join(str(e) for e in self.vector)+']'

    def getUp(self) -> 'State':
        i = self._getEmptyIndex()
        if i >= 3:
            newVector = self.vector.copy()
            newVector[i], newVector[i-3] = newVector[i-3], newVector[i]
            return State(newVector, UP, self)
        else:
            return None

    def getDown(self) -> 'State':
        i = self._getEmptyIndex()
        if i <= 5:
            newVector = self.vector.copy()
            newVector[i], newVector[i+3] = newVector[i+3], newVector[i]
            return State(newVector, DOWN, self)
        else:
            return None

    def getLeft(self) -> 'State':
        i = self._getEmptyIndex()
        if i % 3 != 0:
            newVector = self.vector.copy()
            newVector[i], newVector[i-1] = newVector[i-1], newVector[i]
            return State(newVector, LEFT, self)
        else:
            return None
        
    def getRight(self) -> 'State':
        i = self._getEmptyIndex()
        if i % 3 != 2:
            newVector = self.vector.copy()
            newVector[i], newVector[i+1] = newVector[i+1], newVector[i]
            return State(newVector, RIGHT, self)
        else:
            return None

    def getChildren(self) -> List['State']:
        return [self.getUp(), self.getDown(), self.getLeft(), self.getRight()]

    def getChildrenReverse(self) -> List['State']:
        return [self.getRight(), self.getLeft(), self.getDown(), self.getUp()]

    def isGoal(self) -> bool:
        return self.vector == [0,1,2,3,4,5,6,7,8]
    
    def h(self) -> int:
        sum = 0
        for i in range(1, 9):
            goalRow = i//3
            goalCol = i%3
            curRow = self.vector.index(i)//3
            curCol = self.vector.index(i)%3
            sum += abs(goalRow-curRow) + abs(goalCol-curCol)
        return sum

