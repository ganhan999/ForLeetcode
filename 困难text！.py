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
    def findComplement(self, num: int) -> int:
        bits = len(str(bin(num))) - 2
        return num ^ (2 ** bits - 1)




print(Solution().findComplement(5))
nums=[1,2,3,4,5,6]
print(21//10)