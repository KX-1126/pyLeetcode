import copy
from typing import List

class Solution:
    def printBoard(self, b):
        for i in range(len(b)):
            print(b[i])

    def putQueue(self, i, j, b):
        n = len(b)
        # cross
        for k in range(n):
            b[i][k] = 1
            b[k][j] = 1

        # diagonal
        old_i = i
        old_j = j
        for m in [-1,1]:
            for w in [-1,1]:
                dir = (m,w)
                i = old_i
                j = old_j
                while i+dir[0] < n and i+dir[0] >= 0 and j+dir[1] < n and j+dir[1] >= 0:
                    b[i+dir[0]][j+dir[1]] = 1
                    i = i+dir[0]
                    j = j+dir[1]

        # b[old_i][old_j] = 2

    def isBoardFull(self, b):
        s = 0
        for i in range(len(b)):
           s += sum(b[i])
        if s == 16:
            return True
        else:
            return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        # self.printBoard(board)
        # self.putQueue(2,2,board)
        # self.printBoard(board)

        result = []
        path = []

        def backtracking(n,b):
            if len(path) == n:
                result.append(path[:])
                return result

            for i in range(n):
                for j in range(n):
                    if b[i][j] == 1:
                        continue
                    # if not self.judgeBoard(b):
                    #     continue
                    if self.isBoardFull(b):
                        # path.pop()
                        # b = lastBoard
                        continue
                    lastBoard = copy.deepcopy(b)
                    path.append((i,j))
                    print(path)
                    self.putQueue(i,j,b)
                    backtracking(n,b)
                    path.pop()
                    b = lastBoard

        backtracking(n,board)
        return result

so = Solution()
input1 = 4
f = so.solveNQueens(input1)
print(f)