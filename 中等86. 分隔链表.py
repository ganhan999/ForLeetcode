"""
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

 
示例：
输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5

"""


"""
本体本质就是将链表分为：
1.小于 x 部分的链表按照原始顺序 记为 p
2.大于等于 x 部分的链表按照原始顺序 记为 q
3.拼接两个链表，p --> q
"""
#大神做法1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p=less=ListNode(0)
        q=more=ListNode(0)

        while head:
            if head.val<x:#把所有小于x的排成一个链表
                less.next=head
                less=less.next
            else:#把所有大于等于x的排成一个链表
                more.next=head
                more=more.next
            head=head.next

        more.next=None
        less.next=q.next#两个链表合成一起
        return p.next
