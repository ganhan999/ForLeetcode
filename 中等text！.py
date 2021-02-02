import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res


print(Solution().subsets([1,2,3]))
