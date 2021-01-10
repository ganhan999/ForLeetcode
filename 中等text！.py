import collections
from typing import List
from collections import deque
# import math


from typing import List

from typing import List



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 1
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i +1 + nums[i])
                if rightmost >= n :
                    return True
        return False

print(Solution().canJump([4,2,1,0,4]))

