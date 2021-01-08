import collections
from typing import List
from collections import deque
# import math


from typing import List

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            print(list(zip(*matrix)))
            matrix = list(zip(*matrix))[::-1]
        return res
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

