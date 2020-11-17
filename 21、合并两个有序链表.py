"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""

"""
思路分析：
创建一个新链表，将小的那个值依次填入新链表的next中，直到一个链表为空后，直接将另外一个链表填入新链表的next中。
值得一提的是必须需要建立一个哑节点，不然新链表在执行的时候端点会跑到后面去。
这道题非常类似与归并排序
"""
#我的做法
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newlist=ListNode(0)#起始值为0，没有任何意义，下一个next才是开始。
        yajiedian = newlist#哑巴节点，初始节点！
        while l1 and l2 :
            if l1.val<=l2.val:
                newlist.next=l1#可以使用这样更快的方式运行  node.next,l1 = l1,l1.next
                l1=l1.next
            else:
                newlist.next=l2#node.next,l2 = l2,l2.next
                l2=l2.next
            newlist=newlist.next
        if l1:
            newlist.next=l1
        else:
            newlist.next=l2
        return yajiedian.next


#大神做法

"""
利用递归，把最小的那个值取出来赋给L1，然后到最后会有一个链表为空，于是把那个链表直接赋给l1
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2



"""
python没有指针哪来的链表？

class Node(object):
    #节点
    def __init__(self, val):
        self.val = val#节点的值
        self.next = None#节点的指针（指向下一个Node）
        
在大神做法中，print出来的链表形式是这样的。
None
ListNode{val: 4, next: ListNode{val: 4, next: None}}
ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}
ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}
ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: None}}}}}}

"""