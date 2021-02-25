"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""


"""
迭代
"""
#大神做法1
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head: return
        pre = head
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head





"""
双指针

1、设置两个指针分别指向头节点，pre （记录要删除节点的前一节点）和 cur (记录当前节点)；
2、遍历整个链表，查找节点值为 val 的节点，找到了就删除该节点，否则继续查找。

"""

#大神做法2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        pre, cur = head, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return head



