"""
给你一个长度为n的整数数组，请你判断在 最多 改变1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的：对于数组中任意的i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。



"""


""" 
当 i > 1 且 nums[i] < nums[i - 2]时，我们无法调整 nums[i - 1]，我们只能调整 nums[i] 到 nums[i - 1]。
class Solution(object):
"""
def checkPossibility(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    N = len(nums)
    count = 0
    for i in range(1, N):
        if nums[i] < nums[i - 1]:
            count += 1
            if i == 1 or nums[i] >= nums[i - 2]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return count <= 1

