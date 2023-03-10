import copy
from typing import List

class Solution:
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]

        result = []
        result_str = []
        path = []

        def backtracking(n,b,row_i):
            if len(path) == n:
                result.append(path[:])
                return result

            for j in range(n):
                if b[row_i][j] == 1:
                    continue
                lastBoard = copy.deepcopy(b)
                default_str = "." * len(b)
                path.append(default_str[:j] + "Q" + default_str[j+1:])
                # print(path)
                self.putQueue(row_i,j,b)
                backtracking(n,b,row_i+1)
                path.pop()
                b = lastBoard

        backtracking(n,board,0)
        return result

so = Solution()
input1 = 4
f = so.solveNQueens(input1)
print(f)