"""
给定一个非空且只包含非负数的整数数组nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。


示例 1：
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2：
输入：[1,2,2,3,1,4,2]
输出：6

"""


""" 
使用 left和 right 分别保存了每个元素在数组中第一次出现的位置和最后一次出现的位置；使用 counter保存每个元素出现的次数。
数组的度 degree 等于 counter.values()的最大值；

对counter再次遍历：
如果元素 k出现的次数等于 degree，则找出元素 k最后一次出现的位置 和 第一次出现的位置，计算两者之差+1，即为子数组长度。
对所有出现次数等于 degree 的子数组的最短长度，取 min。

"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = dict(), dict()
        counter = collections.Counter()
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1
        degree = max(counter.values())
        res = len(nums)
        for k, v in counter.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res
