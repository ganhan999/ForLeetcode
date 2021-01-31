import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p=less=ListNode(0)
        q=more=ListNode(0)
        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                more.next=head
                more=more.next
            head=head.next

        more.next=None
        less.next=q.next
        return p.next


print(Solution().deleteDuplicates([1,2,3,3,4,4,5]))
