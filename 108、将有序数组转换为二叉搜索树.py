"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5


"""

"""
思路分析：
DFS，递归，用二分的思想。
"""
#我的做法

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        maxlength=len(nums)
        def DFS(left,right):
            if left>right:
                return
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=DFS(left,mid-1)
            root.right=DFS(mid+1, right)
            return root
        return DFS(0, maxlength-1)





