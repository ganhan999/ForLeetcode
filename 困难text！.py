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
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table_m = collections.Counter(magazine)
        hash_table_r = collections.Counter(ransomNote)

        """for i in hash_table_r:
            if hash_table_r[i] > hash_table_m[i]:
                return False
        return True"""
        return not hash_table_r - hash_table_m



print(Solution().canConstruct("aa","aab"))
