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
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition( left, right):
            tmp = nums[left]
            while left < right:
                while left < right and nums[right] <= tmp:
                    right = right - 1
                nums[left] = nums[right]
                while left < right and nums[left] >= tmp:
                    left = left + 1
                nums[right] = nums[left]
            nums[left] = tmp
            mid = left
            return mid

        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1

print(Solution().findKthLargest([3,5,3,1,2,4,5,6,1],4))
