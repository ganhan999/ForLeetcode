import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret



print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
