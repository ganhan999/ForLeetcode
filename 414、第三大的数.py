"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。



示例 1：
输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。

示例 3：
输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。



"""


"""
转成字典再转列表再排序
"""
#大神做法1
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        return nums[-1] if len(nums) <= 2 else nums[-3]




"""
小顶堆
"""
#大神做法2
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # time O(nlog3) = O(n), space O(n)
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        nums = list(nums)

        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > 3:
                heapq.heappop(pq)

        return pq[0]



"""
快速排序
最差的可能性， time O(n^2), space O(n)
加入随机变量后, time O(n), space O(logn)
一种减而治之的思想。搜索区域中是否匹配到k-1（topk的索引）
partition 可以灵活应变，前面大后面小，或者前面小后面大。
"""
#大神做法2
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # time O(nlog3) = O(n), space O(n)
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        nums = list(nums)

        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > 3:
                heapq.heappop(pq)
        return pq[0]

