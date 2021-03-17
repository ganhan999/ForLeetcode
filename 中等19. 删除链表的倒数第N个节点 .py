"""
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.


"""

"""
一种容易想到的方法是，我们首先从头节点开始对链表进行一次遍历，
得到链表的长度 LL。随后我们再从头节点开始对链表进行一次遍历，
当遍历到第 L-n+1L−n+1 个节点时，它就是我们需要删除的节点。
"""
#我的做法
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getlength(head):
            length=0
            while head:
                length+=1
                head=head.next
            return length
        dummy=ListNode(0,head)
        length=getlength(head)
        cur=dummy
        for i in range(1,length-n+1):
            cur=cur.next
        cur.next=cur.next.next
        return dummy.next

#大神做法1

"""
用栈

我们也可以在遍历链表的同时将所有节点依次入栈。
根据栈「先进后出」的原则，我们弹出栈的第 n 个节点就是需要删除的节点，
并且目前栈顶的节点就是待删除节点的前驱节点。这样一来，删除操作就变得十分方便了。

"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next



#大神做法2

"""
快慢指针
快指针先走n个节点，然后再通知遍历，这样当快指针到最后的时候，慢指针指向了倒数第n个结点。
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


