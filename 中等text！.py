import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools


class Solution(object):
    def removeDuplicates(self, nums):
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j


print(Solution().removeDuplicates([1,1,1,1,2,2,2,3]))
