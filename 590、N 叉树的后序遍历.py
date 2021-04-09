"""

给定一个 N 叉树，返回其节点值的 后序遍历 。
N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。


进阶：
递归法很简单，你可以使用迭代法完成此题吗?

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]



"""


"""
递归
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #保存节点值
        result = []
        #后序遍历
        def pre_order(root):
            #跟节点非空入队列递归遍历
            if root:
                #递归遍历
                for node in root.children:
                    pre_order(node)
                #节点值入队列
                result.append(root.val)
        pre_order(root)
        return result



"""
迭代
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]

