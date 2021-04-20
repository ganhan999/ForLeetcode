"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True


案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

"""


""" 
二叉树中旬遍历得到有序数组 双指针查找
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        def mid_order(root):
            if root:
                mid_order(root.left)
                nums.append(root.val)
                mid_order(root.right)
        mid_order(root)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return False
