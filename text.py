from typing import List
from collections import deque
# import math
'''
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        li = [[1], [1, 1]]
        i = 3
        while True:
            new = []
            for j in range(i - 2):
                new.append(li[i - 2][j] + li[i - 2][j + 1])
            new.insert(0, 1)
            new.append(1)
            li.append(new)
            if rowIndex == i - 1:
                return li[i - 1]
            i = i + 1

print(Solution().getRow(3))

