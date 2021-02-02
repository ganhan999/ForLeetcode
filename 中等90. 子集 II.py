"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


"""
回溯
"""
#大神做法1
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        def back_func(start=0, temp=[]):
            res.append(temp[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                back_func(i+1, temp)
                temp.pop()
        back_func()
        return res

"""
迭代
"""
#大神做法2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [ sorted([num] + i) for i in ans if sorted([num] + i) not in ans]
        return ans
