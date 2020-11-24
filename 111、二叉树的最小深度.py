"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

 
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5



"""
"""
思路分析：
DFS,递归大法，分情况讨论（节点为空，左右节点为空，仅左节点为空等等）
"""
#我的做法

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))

#大神做法

"""
BFS，看左右子树的节点谁先没有左右节点，就停止循环。
"""


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
                print(depth)
            if node.right:
                q.append((node.right, depth + 1))
                print(depth)
        return 0

