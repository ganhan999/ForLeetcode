"""
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。


进阶：
你能用 O(1)（即，常量）内存解决此问题吗？


示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

"""


"""
给head一个属性，flag记录被遍历过的元素，如果发现被遍历过一次，那么就表示有回路
"""
#我的做法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            try:
                if head.flag==1:
                    return True
            except:
                head.flag=1
            head=head.next
        else:
            return False
#大神做法1

"""
哈希表，和我的方法差不多
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 1. python map
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False


#大神做法2

"""
快慢指针法：
枚举时添加一个慢一拍的指针，如果有环最终两个指针会相遇，可能会很慢啊
"""
class Solution:
    def singleNumber(nums):
        return sum(set(nums))*2-sum(nums)


#大神做法3
"""
链表中最多10000个节点，超过10000就是有环
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 3. 计数 10000
        count = 0
        while head and count <= 10000:
            count += 1
            head = head.next
        return count > 10000

