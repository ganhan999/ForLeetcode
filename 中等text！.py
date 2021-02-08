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
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dg(root,-(2**32),2**32) #这里我直接粗暴地将最小值和最大值设置为一个足够小（大）的数，你可以设置你认为的最优解
    def dg(self,root,min_v,max_v):
    # 参数：root：当前节点，min_v：允许最小值（下界），max_v：允许最大值（上界）

        if root == None: # 如果当前节点为空，证明已经递归到叶子节点，返回True
            return True

        if root.val < max_v and root.val > min_v : # 如果当前节点值符合规定，继续进行之后的递归
            pass
        else: # 如果不符合规定，之间返回 False
            return False

        if self.dg(root.left,min_v,root.val) == False: # 对左子树进行递归，此时最大值应该为当前节点值
            return False
        if self.dg(root.right,root.val,max_v) == False:# 对右子树进行递归，此时最小值应该为当前节点值
            return False

        return True # 如果成功避开所有坑，恭喜，这个当前节点下的子树是一个二叉搜索树



print(Solution().subsets([1,2,3]))
