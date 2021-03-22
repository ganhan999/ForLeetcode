"""
给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加 1。找出让数组所有元素相等的最小操作次数。


示例：
输入：
[1,2,3]

输出：
3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]



"""


"""
数学题

假设目前数组总和为sum，我们需要移动次数为m，那么整体数组总和将会增加m * (n - 1)，这里的n为数组长度，最后数组所有元素都相等为x，于是有：
sum + m * (n - 1) = x * n (1)
我们再设数组最小的元素为min_val，m = x - min_val，即 x = m + min_val带入(1)得：
m = sum - min_val * n


"""
#大神做法1
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)





