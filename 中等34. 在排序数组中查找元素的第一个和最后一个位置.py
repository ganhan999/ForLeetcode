"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。

进阶：
你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？


示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]



"""

"""
二分查找，先找左边的数，如果mid等于target那么右边的target不可能是最左边的数。反之亦然。

"""

#大神做法1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]
        first_position = self.__find_first_position(nums, size, target)
        if first_position == -1:
            return [-1, -1]
        last_position = self.__find_last_position(nums, size, target)
        return [first_position, last_position]

    def __find_first_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            else:
                # nums[mid] > target
                right = mid - 1

        if nums[left] == target:
            return left
        else:
            return -1

    def __find_last_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right + 1) // 2   #这里是因为如果存在8，8的情况，那么需要去上整数才可以得到最右边的数
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid
            else:
                # nums[mid] < target
                left = mid + 1
        # 由于能走到这里，说明在数组中一定找得到目标元素，因此这里不用再做一次判断  因为左边已经找到了数
        return left

