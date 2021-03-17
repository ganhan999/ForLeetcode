"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例1:
输入: 1->1->2
输出: 1->2

示例2:
输入: 1->1->2->3->3
输出: 1->2->3


"""

"""
思路分析：
删除链表操作而已。

"""
#我的做法
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head#注意这里是引用地址，标记这初始地址，但是next是调用属性，所以操作node实际上就是改变了head链表，head还是一开始的地址，但是node已经不是了
        while node and node.next:#注意先把node放前面，因为如果node为空，node会出现断路现象，保护后面next条件不报错
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head#返回初始地址！所以不能用node

#大神做法1

"""
双指针算法
建议自己多画画图就知道了，用a来遍历整个链表，用head来改变整个链表。
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head_copy = head
        a = head
        while a:
            if a.val == head.val:
                a = a.next
                if a.next is None:
                    if a.val == head.val:
                        head.next = None
                    else:
                        head.next = a
                    break
            else:
                head.next = a
                head = head.next

        return head_copy



