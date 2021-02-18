"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3


"""


"""
中序遍历后查找
"""
#大神做法1
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]






"""
利用迭代就可以不用全部遍历二叉树
"""
#大神做法2
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


