"""

给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。


示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

"""


"""
中序遍历 然后记录每一次的最小差值
"""
#大神做法1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        #初始化，最小值赋值为无穷大，last_value记录上一个节点的值
        min_value, last_value = float("inf"), -1
        def pengding_num(val):
            nonlocal min_value, last_value
            #第一个节点赋值给last_value
            if last_value == -1:
                last_value = val
            else:
                #每次求差的绝对值的最小值，更新
                min_value = min(min_value, abs(val - last_value))
                last_value = val
        #中序遍历
        def mid_order(root):
            nonlocal min_value, last_value
            if root:
                mid_order(root.left)
                #处理当前节点
                pengding_num(root.val)
                mid_order(root.right)
        mid_order(root)
        return min_value




