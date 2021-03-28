"""
给定一个二进制数组， 计算其中最大连续 1 的个数。

示例：
输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

"""


"""
为了得到数组中最大连续 1 的个数，需要遍历数组，并记录最大的连续 1 的个数和当前的连续 1 的个数。如果当前元素是 1，
则将当前的连续 11 的个数加 11，否则，使用之前的连续 11 的个数更新最大的连续 1 的个数，并将当前的连续 1 的个数清零。

遍历数组结束之后，需要再次使用当前的连续 1 的个数更新最大的连续 1 的个数，
因为数组的最后一个元素可能是 1，且最长连续 1 的子数组可能出现在数组的末尾，如果遍历数组结束之后不更新最大的连续 1 的个数，则会导致结果错误。

"""
#大神做法1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0

        maxCount = max(maxCount, count)
        return maxCount



"""
记录零的位置
"""
#大神做法2
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                res = max(res, i - index)
        return res

