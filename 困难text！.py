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
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.help = deque()
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help,self.data = self.data,self.help
        return tmp
    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.data) != 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help.append(tmp)
        self.help,self.data = self.data,self.help
        return tmp
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.data)





print(Solution().containsNearbyDuplicate([1,2,3,1],3))
