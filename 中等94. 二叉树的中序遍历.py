"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[2,1]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

"""


"""
递归

"""
#大神做法1
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            # 递归完左子树后，处理节点值
            ans.append(root.val)
            inorder(root.right)
        ans = []
        inorder(root)
        return ans



"""
利用栈
"""
#大神做法2
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while stack or root:
            if root:
                # 这部分将左子树压入栈中
                stack.append(root)
                root = root.left
            else:
                # 进入右子树前处理值
                tmp = stack.pop()
                ans.append(tmp.val)
                # 进入右边第一个子树，继续循环
                root = tmp.right
        return ans


