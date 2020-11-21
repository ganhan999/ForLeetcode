"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true


示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false


示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false



"""

"""
思路分析：
递归大法好。
一句话, 先想出口：
    空的话怎么办？
    一个出口怎么办？
    通常情况下怎么处理当前元素, 同时减少问题规模？

"""
#我的做法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


#大神做法1

"""
深度优先遍历，把遍历的数字加入数组中。
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        resp, resq = [], []
        self.DFS(p, resp)
        self.DFS(q, resq)
        return resp == resq

    def DFS(self, tree, res):
        if not tree:
            res.append('')
            return
        res.append(tree.val)#先序遍历
        self.DFS(tree.left, res)
        self.DFS(tree.right, res)


