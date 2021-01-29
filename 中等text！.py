import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[0] <= nums[mid]:        # mid在左半边有序数组
                if nums[0] <= target < nums[mid]:   # 并且目标在左半边有序数组中
                    right = mid - 1
                else:
                    left = mid + 1
            else:                           # mid在右半边有序数组
                if nums[mid] < target <= nums[-1]:  # 并且目标在右半边有序数组中
                    left = mid + 1
                else:
                    right = mid - 1
        return False
print(Solution().search([2,5,6,0,0,1,2],0))
