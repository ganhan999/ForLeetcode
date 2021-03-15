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
    def readBinaryWatch(self, num: int) -> List[str]:
        hours = [1, 2, 4, 8, 0, 0, 0, 0, 0, 0]
        minutes = [0, 0, 0, 0, 1, 2, 4, 8, 16, 32]
        res = []
        def backtrack(num, index, hour, minute):
            if hour > 11 or minute > 59:
                return
            if num == 0:
                res.append('%d:%02d' % (hour, minute))
                return
            for i in range(index, 10):
                backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i])

        backtrack(num, 0, 0, 0)
        return res

print(Solution().readBinaryWatch(6))
