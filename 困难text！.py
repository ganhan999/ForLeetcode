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
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1=set(list1)
        l2=set(list2)
        l12=l1&l2
        res=[]
        tmp=float('inf')
        for i in l12:
            tmp=min(tmp,list1.index(i)+list2.index(i))
        for i in l12:
            if list1.index(i)+list2.index(i)==tmp:
                res.append(i)
        return res





print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
