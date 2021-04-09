"""

给定一个 N 叉树，返回其节点值的 前序遍历 。
N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。


进阶：
递归法很简单，你可以使用迭代法完成此题吗?


示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]

"""


"""
递归
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)

        helper(root)

        return res



"""
迭代
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]                                  #初始化一个数据
        out = []
        while stack:
            temp = stack.pop()                          #先把栈顶的数据弹出来加入到 输出 集
            out.append(temp.val)
            if temp.children:                           #如果该元素有子节点children 则反转加入到 stack 里(因为是前序遍历)
                for item in temp.children[::-1]:
                    stack.append(item)
        return out

