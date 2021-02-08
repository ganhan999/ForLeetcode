"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

"""


"""
链表转列表
"""
#我的做法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


#大神做法1
"""
整个流程可以分为以下五个步骤：

找到前半部分链表的尾节点。
反转后半部分链表。
判断是否回文。
恢复链表。
返回结果。
"""

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        cur = slow.next
        slow.next = None
        while cur:#反转链表
            tmp = cur.next
            cur.next = pre
            pre = cur #pre指向前一个指针
            cur = tmp
        while pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True




