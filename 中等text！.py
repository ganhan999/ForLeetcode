from typing import List
from collections import deque
# import math


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        grid = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    tmp = int(board[i][j])
                    row[i][tmp] = row[i].get(tmp, 0) + 1#如果已经存在该数字，那么就继续加一，没有就从0开始
                    col[j][tmp] = col[j].get(tmp, 0) + 1
                    grid[i//3][j//3][tmp] = grid[i//3][j//3].get(tmp, 0) + 1
                    if row[i].get(tmp) > 1 or col[j].get(tmp) > 1 or grid[i//3][j//3].get(tmp) > 1:#如果对应的value大于1说明，存在两次，直接退出循环
                        return False
        return True

print(Solution().isValidSudoku([["5","3","3",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
