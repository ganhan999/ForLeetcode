"""
计算给定二叉树的所有左叶子之和。

示例：
    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


"""


"""
递归 DFS
"""
#大神做法1
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def dfs(root, flag=False):  # 初始化flag = False
            if not root: return 0  # 先判断root是否为None，否则下面的判断语句会报错
            if not root.right and not root.left and flag:  # 前两个条件保证是否是叶子节点，flag保证是否是左孩子
                return root.val  # 如果是左叶子结点就加上其值
            return dfs(root.right, False) + dfs(root.left, True)  # 递归root的左孩子并让flag = True, 右孩子flag = False

        return dfs(root)  # 返回结果

"""
BFS 广度优先遍历  也是放一个标志位表示左节点
"""
#大神做法2
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root, flag=False):  # 初始化flag = False
            if not root: return 0  # 先判断root是否为None，否则下面的判断语句会报错
            if not root.right and not root.left and flag:  # 前两个条件保证是否是叶子节点，flag保证是否是左孩子
                return root.val  # 如果是左叶子结点就加上其值
            return dfs(root.right, False) + dfs(root.left, True)  # 递归root的左孩子并让flag = True, 右孩子flag = False
        return dfs(root)  # 返回结果
