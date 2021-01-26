import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res
print(Solution().subsets([1,2,3]))
