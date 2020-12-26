"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。


示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]



"""

"""
以358764为例
1、从右到左，找到第一个左侧小于右侧的下标值i
2、再次从右到左，找到第一个大于nums[i]的数以及下标j，然后i 和 j对应的数进行互换
3、i下标后面的数按从小到大排序

时间复杂度O(n)
空间复杂度为O(1)

"""
#大神做法1
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        # 记录是否存在下一个更大的排列
        begin = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                # 第一种情况：最后两个数颠倒位置
                if i == len(nums) - 2:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    return
                # 第二种情况：排序后找到可以替换当前位置的数字
                else:
                    self.reverse(nums, begin)
                    j = bisect.bisect(nums, nums[begin - 1], lo=begin)
                    nums[i], nums[j] = nums[j], nums[i]
                    return
            else:
                begin = i
        if begin == 0:
            self.reverse(nums)

    def reverse(self, nums, begin=0):
        length = len(nums) - 1
        while begin < length:
            nums[begin], nums[length] = nums[length], nums[begin]
            begin += 1
            length -= 1


