"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。



示例 1：
输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。

示例 2：
输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。


"""


""" 
实际上我们通过题意可以得知，最小的元素一定的根节点，所以我们只要找到比根节点大的节点，
直接返回就行了，更不用继续遍历当前节点下面的子节点，因为子节点的值不可能比它还小。
"""
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """前序遍历"""
        def helper(root, val):
            if not root:
                return -1

            if root.val > val:#如果是 222 的情况 那么就会子节点还是会返回-1  val是不变的  一旦找到第一个比根节点大的就返回
                return root.val
            left = helper(root.left, val)
            right = helper(root.right, val)
            if left < 0: return right
            if right < 0: return left
            return min(left, right)

        return helper(root, root.val)

