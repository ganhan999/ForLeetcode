"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。


示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true


"""

"""
思路分析：
递归每一个节点的平衡因子，如果绝对值小于2，那么就平衡。
用到了求最大深度的函数。
"""
#我的做法

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.right)-self.height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
	# 求高度
    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.right),self.height(node.left))


#大神做法

"""
利用字典保存，最大深度的值，可以减少递归次数。
"""


class Solution:
    dct = {}
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def maxDepth(root: TreeNode) -> int:
            if not root:
                return 0
            if root not in self.dct:
                self.dct[root] = 1 + max(maxDepth(root.left), maxDepth(root.right))
            return self.dct[root]

        tmp = maxDepth(root.left) - maxDepth(root.right)
        return abs(tmp)<2  and self.isBalanced(root.left) and self.isBalanced(root.right)


#大神做法2

"""
在求取左右子节点时，判断子节点是否失衡，
如果失衡则无需求根节点的平衡度，向上通知提前退出递归。
因为-1表示递归提前退出或者失衡.
如果左子树已经出现了失衡状况，就只会遍历一半！！！
在算深度的时候，就把平衡的条件给判定了。
"""
class Solution:
    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        if left < 0: return -1#左子树失衡
        right = self.height(root.right)
        if right < 0 : return -1#右子树失衡
        if abs(left - right) > 1:
            return -1#当前节点失衡
        return max(left, right) + 1#平衡，继续递归

    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0


#大神做法3
"""
自底向上
通过直接判断左右子树高度，改变res参数，递归仍然会进行完毕
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            #print(right, left)
            if abs(right - left) > 1:
                self.res = False
            return max(left, right)
        helper(root)
        return self.res

