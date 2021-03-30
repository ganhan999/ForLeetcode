"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].



"""


"""
中序遍历后再操作
"""
#大神做法1
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        base = None
        count = 0
        maxCount = 0

        def update(x):
            nonlocal base, count, maxCount, ans
            if x == base:
                count += 1
            else:
                base = x
                count = 1
            if count == maxCount:
                ans.append(x)
            elif count > maxCount:
                maxCount = count
                ans.clear()
                ans.append(x)

        def midtraverse(node):
            if not node:
                return
            midtraverse(node.left)
            update(node.val)
            midtraverse(node.right)

        midtraverse(root)
        return ans
