"""
给定一个范围在 1 ≤ a[i] ≤ n (n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]


"""


"""
本题最简单的方法就是，对 1-n1−n 的所有数字进行遍历，判断每个数字是否在数组中存在。
问题是如何快速判断数字在数组中存在吗？可以使用 set数据结构，它的查找时间复杂度可以降低到 O(1)
"""
#大神做法1
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = set(nums)
        N = len(nums)
        res = []
        for i in range(1, N + 1):
            if i not in counter:
                res.append(i)
        return res




"""
由于 nums 的数字范围均在 [1,n] 中，我们可以利用这一范围之外的数字，来表达「是否存在」的含义。

具体来说，遍历 nums，每遇到一个数 x，就让 nums[x−1] 增加 nn。由于 nums 中所有数均在 [1,n] 中，增加以后，这些数必然大于 n。
最后我们遍历 nums，若nums[i] 未大于 n，就说明没有遇到过数 i+1。这样我们就找到了缺失的数字。

注意，当我们遍历到某个位置时，其中的数可能已经被增加过，因此需要对 n 取模来还原出它本来的值。

"""
#大神做法2
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n

        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret




