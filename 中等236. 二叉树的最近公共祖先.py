"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1



"""


"""
递归 
把符合条件的搬到父节点
"""
#大神做法1
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # 边界条件，如果匹配到left或right就直接返回停止递归
        if root.val == p.val or root.val == q.val:
            return root
        # 这两行代码可以无脑先写好！
        # 因为是DFS算法，这个模板可以无脑套用，写上之后可能你思路就清晰很多
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果既在左子树找到，又在右子树找到，那么毫无疑问当前root就是公共节点
        if left and right:
            return root
        # 只有左子树有，那么直接返回左子树匹配到的第一个节点
        if left:
            return left
        if right:
            return right
