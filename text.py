from typing import List
from collections import deque
# import math
import re

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return 0
        m = {}
        m=self.bianli(headA,m)
        ans=self.bianli(headB,m)
        return ans
    def bianli(self,head,m):
        while head:
            if m.get(head):
                return head.val
            m[head] = 1
            head = head.next
        else:
            return m
headA=ListNode(1)
a=ListNode(1)
headA.next=a
print(a==)


headB=ListNode(2)
b=ListNode(1)
headB.next=b


print(Solution().getIntersectionNode(headA, headB))