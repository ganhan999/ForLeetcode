import collections
from typing import List
from collections import deque
# import math
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:#如果p0 < p1，要把nums[i], nums[p1]互换，当 p_0 < p_1时，我们已经将一些1连续地放在头部，此
                    # 时一定会把一个 11 交换出去，导致答案错误
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1



print(Solution().sortColors([2,0,2,1,1,0]))
