from typing import List
from collections import deque
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, p1, p2):
        if not p1 and not p2:
            return True
        if not p1 or not p2:  # 左右子树都空的情况上面已经排除
            return False
        return p1.val == p2.val and self.isMirror(p1.left, p2.right) and self.isMirror(p1.right, p2.left)


print(math.log(10, 2))