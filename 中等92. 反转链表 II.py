"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤m≤n≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL


"""


"""
用三个指针,进行插入操作

例如:

1->2->3->4->5->NULL, m = 2, n = 4

将节点3插入节点1和节点2之间

变成: 1->3->2->4->5->NULL

再将节点4插入节点1和节点3之间

变成:1->4->3->2->5->NULL

实现翻转的效果!


"""
#大神做法1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    class Solution:
        def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
            dummy = ListNode(-1)
            dummy.next = head
            pre = dummy
             # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
            for _ in range(m - 1):
                pre = pre.next
            # 用 pre, start, tail三指针实现插入操作
            # tail 是插入pre,与pre.next的节点
            start = pre.next
            tail = start.next
            for _ in range(n - m):
                start.next = tail.next
                tail.next = pre.next
                pre.next = tail
                tail = start.next
            return dummy.next


"""
找到要翻转部分的链表,将其翻转,再与原链表拼接;

直接看代码注释.
"""
#大神做法2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
        for _ in range(m-1):
            pre = pre.next
        # 用双指针,进行链表翻转
        node = None
        cur = pre.next
        for _ in range(n-m+1):
            tmp = cur.next
            cur.next = node
            node = cur#node是头节点
            cur = tmp#cur是原链表的下一个节点
        # 将翻转部分 和 原链表拼接
        pre.next.next = cur
        pre.next = node
        return dummy.next

