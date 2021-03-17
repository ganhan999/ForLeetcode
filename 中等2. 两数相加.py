"""
给出两个非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807



"""


"""
因为两个数字相加会产生进位，所以使用i来保存进位。
则当前位的值为(l1.val + l2.val + i) % 10
则进位值为(l1.val + l2.val + i) / 10
建立新node，然后将进位传入下一层。

"""
#我的做法
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def DFS(l1,l2,i):
            if not l1 and not l2 and not i:
               return None
            s=(l1.val if l1 else 0)+(l2.val if l2 else 0)+i
            node=ListNode(s%10)
            node.next=DFS(l1.next if l1 else None,l2.next if l2 else None,s//10)
            return node
        return DFS(l1,l2,0)




