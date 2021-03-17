"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。

说明:叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。



"""
"""
思路分析：
DFS,一直向下找到叶子节点，如果到叶子节点时sum == root.value，说明找到了一条符合要求的路径。
"""
#我的做法

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

#大神做法1

"""
回溯
这里的回溯指 利用 DFS 找出从根节点到叶子节点的所有路径，
只要有任意一条路径的和等于sum，就返回 True。
下面的代码并非是严格意义上的回溯法，因为没有重复利用 path 变量。
"""


class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        res = []
        return self.dfs(root, sum, [root.val])

    def dfs(self, root, target, path):
        if not root: return False#到末节点都还没有成功，那么就是False
        if sum(path) == target and not root.left and not root.right:#记录了到每一个节点路径长度
            return True
        left_flag, right_flag = False, False
        if root.left:
            left_flag = self.dfs(root.left, target, path + [root.left.val])
        if root.right:
            right_flag = self.dfs(root.right, target, path + [root.right.val])
        return left_flag or right_flag


#大神做法2

"""
BFS使用队列保存遍历到每个节点时的路径和，
如果该节点恰好是叶子节点，并且路径和正好等于sum，说明找到了解。


"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que=collections.deque()
        que.append((root,root.val))
        while que:
            node,path=que.popleft()
            if not node.left and not node.right and path==sum:
                return True
            if node.left:
                que.append((node.left,path+node.left.val))
            if node.right:
                que.append((node.right, path + node.right.val))
        return False


#大神做法3

"""
栈
除了上面的 队列 解法以外，也可以使用 栈，同时保存节点和到这个节点的路径和。
但是这个解法已经不是 BFS。因为会优先访问 后进来 的节点，导致会把根节点的右子树访问结束之后，
才访问左子树。

可能会有朋友好奇很少见到这种写法，为什么代码可行？答案是：栈中同时保存了
(节点，路径和)，也就是说只要能把所有的节点访问一遍，那么就一定能找到正确的结果。
无论是用 队列 还是 栈，都是一种 树的遍历 方式，只不过访问顺序有所有不同罢了。

"""
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False
