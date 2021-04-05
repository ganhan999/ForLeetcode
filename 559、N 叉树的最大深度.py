"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。


示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：3

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：5


"""


"""
解决这个问题的最直观方法就是递归。
此处展示了深度优先搜索的策略。
"""
#大神做法1
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1




"""
我们还可以在堆栈的帮助下将上面的递归转换为迭代。
思路是是使用深度优先搜索策略访问每个节点，同时更新每次访问时的最大深度。
所以可以从包含根节点的、对应深度为 11 的栈开始。
然后继续迭代，从栈中弹出当前节点并将子节点压入栈中，每次都更新对应深度。
"""
#大神做法2
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))

        return depth

