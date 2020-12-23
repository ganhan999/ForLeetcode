"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

"""

"""
我们来一一分析下，假设链表总长是偶数，那么递归函数执行到终止条件时，head 就等于 null。
如果链表链表总长是偶数，那么递归函数执行到终止条件时，head.next 就等于 null。
递归函数内，我们要改变 1->2 的指向，将其改为 2->1。
那后面的节点怎么办呢？不用担心，这是由下一层递归函数来解决。下一层递归函数返回后的节点是 4，
就是4->3->...这样的了，也就是后面的节点都已经串联好了。所以我们只需要将 1 节点指向 4 就可以啦。

递归出口：当前节点或者下一个节点为空，返回
方法内容：当前节点next，指向当前节点，指针互换
返回值：返回交换完成的节点

"""
#大神做法1
class Solution(object):
	def swapPairs(self, head):
		# 递归的终止条件
		if not (head and head.next):
			return head
		# 假设链表是 1->2->3->4
		# 这句就先保存节点2
		tmp = head.next
		# 继续递归，处理节点3->4
		# 当递归结束返回后，就变成了4->3
		# 于是head节点就指向了4，变成1->4->3
		head.next = self.swapPairs(tmp.next)
		# 将2节点指向1
		tmp.next = head
		return tmp





#大神做法2

"""
利用stack
我们利用一个 stack，然后不断迭代链表，每次取出两个节点放入 stack 中，再从 stack 中拿出两个节点。
借助 stack 后进先出的特点，放进去的时候是 1,2 。拿出来的时候就是 2，1 两个节点了。
再把这两个节点串联起来，重复这个逻辑遍历完整个链表，就可以做到两两反转的效果了。
虽然用到了 stack，但因为只存了两个元素，所以空间复杂度还是 O(1)O(1)，时间复杂度是 O(n)O(n)。


"""

class Solution(object):
	def swapPairs(self, head):
		if not (head and head.next):
			return head
		p = ListNode(-1)
		# 用stack保存每次迭代的两个节点
		# head指向新的p节点，函数结束时返回head.next即可
		cur,head,stack = head,p,[]
		while cur and cur.next:
			# 将两个节点放入stack中
			_,_ = stack.append(cur),stack.append(cur.next)
			# 当前节点往前走两步
			cur = cur.next.next
			# 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
			p.next = stack.pop()
			p.next.next = stack.pop()
			p = p.next.next
		# 注意边界条件，当链表长度是奇数时，cur就不为空
		if cur:
			p.next = cur
		else:
			p.next = None
		return head.next
