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

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        if len(s)!= len(pattern):
            return False
        dic = {}
        for i,x in enumerate(s):
            if pattern[i] not in dic:
                if x in dic.values():
                    return False
                dic[pattern[i]] = x
            else:
                if x != dic[pattern[i]]:
                    return False
        return True


print(Solution().wordPattern("abba","dog cat cat dog"))
