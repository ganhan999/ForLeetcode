from typing import List
from collections import deque
# import math


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2: return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[i + 1:] = sorted(nums[i + 1:])
                print(nums)
                return
        return nums.sort()


print(Solution().nextPermutation([1,2,3,4,6,5]))