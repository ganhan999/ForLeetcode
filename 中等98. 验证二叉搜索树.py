"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。



"""


"""
中序遍历后应该是递增序列
"""
#大神做法1
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True



"""
从上往下递归
"""
#大神做法2
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dg(root,-(2**32),2**32) #这里我直接粗暴地将最小值和最大值设置为一个足够小（大）的数，你可以设置你认为的最优解
    def dg(self,root,min_v,max_v):
    # 参数：root：当前节点，min_v：允许最小值（下界），max_v：允许最大值（上界）

        if root == None: # 如果当前节点为空，证明已经递归到叶子节点，返回True
            return True

        if root.val < max_v and root.val > min_v : # 如果当前节点值符合规定，继续进行之后的递归
            pass
        else: # 如果不符合规定，之间返回 False
            return False

        if self.dg(root.left,min_v,root.val) == False: # 对左子树进行递归，此时最大值应该为当前节点值
            return False
        if self.dg(root.right,root.val,max_v) == False:# 对右子树进行递归，此时最小值应该为当前节点值
            return False

        return True # 如果成功避开所有坑，恭喜，这个当前节点下的子树是一个二叉搜索树



