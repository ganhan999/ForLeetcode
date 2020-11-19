"""
给定一个二叉树，检查它是否是镜像对称的。


例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


"""

"""
思路分析：
递归大法，
判断p1的左子树，和p2的右子树是否相等。
值得一提的是，需要将root也一分为二，这样就可以判断根节点了。
这是广度优先遍历了！

"""
#我的做法
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root, root)

    def ismirror(self, p1, p2):
        if not p1 and not p2:
            return True
        if not p1 or not p2:
            return False
        return p1.val == p2.val and self.ismirror(p1.right, p2.left) and self.ismirror(p2.right, p1.left)

#大神做法1

"""
不难发现 post_order 就是 pre_order的逆序，其实这也是对称二叉树的一个性质，
根据这一点就不难写出代码了。
前序遍历等于后序遍历的倒序，则为镜像！（妙啊）
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        bli = []     # 用来存左子树的前序遍历
        fli = []     # 用来存右子树的后序遍历
        if root == None:   # 无根节点
            return True
        if root and root.left == None and root.right == None:  # 只有根节点
            return True

        if root and root.left and root.right:
            self.pre_order(root.left, bli)
            self.post_order(root.right, fli)
            fli.reverse()            # 将后序遍历的列表倒序
            if bli == fli:
                return True
            else:
                return False

    def pre_order(self,root,li):    # 二叉树的前序遍历
        if root:
            li.append(root.val)
            self.pre_order(root.left,li)
            self.pre_order(root.right,li)
        elif root == None:
            li.append(None)

    def post_order(self,root,li):   # 二叉树的后序遍历
        if root:
            self.post_order(root.left,li)
            self.post_order(root.right,li)
            li.append(root.val)
        elif root == None:
            li.append(None)



#大神做法2

"""
迭代方法。
BFS 使用一个队列，很多题解中的 BFS 都是放入了四次节点，一种更直观的做法是两两一组放入队列中。

在队列中同时取出两个节点left, right，判断这两个节点的值是否相等，然后把他们的孩子中按照(left.left, right.right) 一组，(left.right, right.left)一组放入队列中。

BFS做法需要把所有的节点都检查完才能确定返回结果True，除非提前遇到不同的节点值而终止返回False。

"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue=collections.deque()
        queue.append((root.left,root.right))#注意这里只传递了一个参数，他们一起组成了迭代器
        while queue:
            left,right=queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            queue.append((left.left,right.right))
            queue.append((left.right,right.left))
        return True
