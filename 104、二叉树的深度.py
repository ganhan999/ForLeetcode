"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""

"""
思路分析：
递归大法,就相当于深度优先遍历了
画图，找到终止条件为空节点记录为0深度，递归本体是父节点的深度等于子节点的深度最大值加一。
"""
#我的做法
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))#这里就相当于调用了系统栈，进行深度优先遍历
        return ans



#大神做法

"""
迭代方法。
广度优先遍历，也就是层次遍历，每一层便加1.
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            # 保存下一层所有节点
            next_layer = []
            while queue:
                node = queue.popleft()
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            queue = deque(next_layer)
        return depth


