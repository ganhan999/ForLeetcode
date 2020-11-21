from typing import List
from collections import deque
# import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que=deque([root])
        l=[]
        while que:
            nextque=deque()
            l1=[]
            while que:
                num=que.popleft()
                l1.append(num.val)
                print (l1)
                if num.left:
                    nextque.append(num.left)
                if num.right:
                    nextque.append(num.right)
            l.append(l1)
            que=nextque
        l=l[::-1]
        return l
l=[1,[1,2],[1,2,3]]
l.reverse()
print(l)