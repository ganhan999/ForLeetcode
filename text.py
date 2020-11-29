from typing import List
from collections import deque
# import math
import re

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head=ListNode(1)
def nums(head):
        if head.flag==1:
            return
        else:
            head.flag=0


nums(head)