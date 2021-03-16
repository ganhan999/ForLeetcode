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
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hex, ans = "0123456789abcdef",  ""
        while num and len(ans) < 8:
            ans = hex[num & 0xf] + ans
            num >>=  4
            print(num >>4)

        return ans


print(Solution().toHex(-2))
