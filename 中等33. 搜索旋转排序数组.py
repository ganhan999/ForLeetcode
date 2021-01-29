"""
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1


"""

"""
题目要求算法时间复杂度必须是 O(\log n)O(logn) 的级别，这提示我们可以使用二分搜索的方法。

但是数组本身不是有序的，进行旋转后只保证了数组的局部是有序的，这还能进行二分搜索吗？答案是可以的。

可以发现的是，我们将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。
拿示例来看，我们从 6 这个位置分开以后数组变成了 [4, 5, 6] 和 [7, 0, 1, 2] 两个部分，
其中左边 [4, 5, 6] 这个部分的数组是有序的，其他也是如此。

"""

#大神做法1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:        # mid在左半边有序数组
                if nums[0] <= target < nums[mid]:   # 并且目标在左半边有序数组中
                    right = mid - 1
                else:
                    left = mid + 1
            else:                           # mid在右半边有序数组
                if nums[mid] < target <= nums[-1]:  # 并且目标在右半边有序数组中
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

