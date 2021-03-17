"""
编写一个程序，找到两个单链表相交的起始节点。

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例2：
输入：intersectVal= 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。


注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。




"""


"""
将所有A的节点记录在字典中，再用B去查找，如果找到了则返回节点
"""
#我的做法
class MinStack:
    class Solution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            if headA is None or headB is None:
                return None
            m = {}
            m = self.bianli(headA, m)
            ans = self.bianli(headB, m)
            return None if (isinstance(ans, dict)) else ans

        def bianli(self, head, m):
            while head:
                if m.get(head):
                    return head
                m[head] = 1
                head = head.next
            else:
                return m
#大神做法1

"""
用集合，但不是用字典，思路差不多
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = set()
        cur1 = headA
        cur2 = headB
        while cur1:
            A.add(cur1)
            cur1 = cur1.next
        while cur2:
            if cur2 in A:
                return cur2
            cur2 = cur2.next
        return None




#大神做法2

"""
分别遍历两个链表，并记录两链表的长度差n，将出现两种情况，
(1)让长链表先走n步
(2)再同时开始走，并对比两个链表的当前节点，节点相等时即为交点
(3)若没有交点，则在最后的Null处相交


"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        n = 0
        while cur1:
            n += 1
            cur1 = cur1.next
        while cur2:
            n -= 1
            cur2 = cur2.next
        if cur1 != cur2:
            return None
        cur1 = headA if n > 0 else headB
        cur2 = headB if cur1 == headA else headA
        n = abs(n)
        while n:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

#大神做法3

"""
长短链表相互拼接，遇到相同节点跳出循环，该节点即为相交节点

"""
class Solution:
    def getIntersectionNode(self, L1: ListNode, L2: ListNode) -> ListNode:
        h1, h2 = L1, L2
        while h1 is not h2:
            h1 = h1.next if h1 else L2
            h2 = h2.next if h2 else L1
        return h1

