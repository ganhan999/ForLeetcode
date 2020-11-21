"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""

"""
思路分析：
BFS，每一层都放在一个队列当中
"""
#我的做法
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que=deque([root])
        l=[]
        while que:
            nextque=[]
            l1=[]
            while que:
                num=que.popleft()
                l1.append(num.val)
                if num.left:
                    nextque.append(num.left)
                if num.right:
                    nextque.append(num.right)
            l.append(l1)
            que=deque(nextque)
        l.reverse()
        return l



#大神做法

"""
深度优先遍历，因为每找到一个左右节点，层数就加一层，记录层数depth，将depth作为下标。
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res)<depth+1:#每多一层那么就加一个元素列表
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,0)
        return res[::-1]



