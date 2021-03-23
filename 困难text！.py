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
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ##典型的贪心算法：先排序，倒序最好。让最大饼干的满足最贪心的小朋友，如果当前的饼干不能满足当前的小朋友，就找下一个小朋友看是否能满足
        gi = 0 ## g:小朋友的胃口，也就是贪心值
        si = 0 ## s:饼干值
        g.sort(reverse=True) ##倒序输出
        s.sort(reverse=True)
        res = 0
        lens_g = len(g)
        lens_s = len(s)
        while gi<lens_g and si<lens_s:
            if s[si]>=g[gi]:
                res+=1
                si+=1
                gi+=1
            else:
                gi+=1 ##看一下小朋友的胃口是否能满足当前的饼干
        return res


print(Solution().findContentChildren([1,2,3],[1,2]))
