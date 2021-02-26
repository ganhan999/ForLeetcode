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
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 创建哈希表
        hash_map = {}
        # 遍历一次数组
        for idx, n in enumerate(nums):
            if n not in hash_map or (idx - hash_map[n]) > k:  # 情况1 & 情况2
                hash_map[n] = idx
            else:  # 情况3
                return True
        else:
            return False




print(Solution().containsNearbyDuplicate([1,2,3,1],3))
