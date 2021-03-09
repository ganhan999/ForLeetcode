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
    def isSubsequence(self, s: str, t: str) -> bool:
        hashmap = {}
        for i, c in enumerate(t):
            if c not in hashmap:
                hashmap[c] = [i]
            else:
                hashmap[c].append(i)

        j = 0
        for i in range(len(s)):
            c = s[i]
            if c not in hashmap:
                return False
            pos = self.find_left(hashmap[c], j)  # 二分搜索与c匹配的下一个索引，避免线性扫描
            if pos >= len(hashmap[c]):#如果超过了 那么不可能匹配
                return False
            j = hashmap[c][pos] + 1
        return True

    def find_left(self, index, target):
        left, right = 0, len(index) - 1
        while left <= right:
            mid = (left + right) // 2
            if index[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


print(Solution().isSubsequence("abc","abbadc"))
