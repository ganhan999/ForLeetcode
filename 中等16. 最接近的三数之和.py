"""
给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

"""

"""
和上一题差不多，排序＋双指针法，排序后可以化简为双指针的twosum题   
"""
#我的做法
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        d = float('inf')
        for i in range(n):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                x = (nums[i] + nums[L] + nums[R]) - target
                if (nums[i] + nums[L] + nums[R] == target):
                    return nums[i] + nums[L] + nums[R]
                if abs(x)<d:
                    ans = nums[i] + nums[L] + nums[R]
                    d=abs(x)
                if x>0:
                    R=R-1
                else:
                    L = L + 1
        return ans