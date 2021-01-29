"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false


"""



"""
这道题和33题一样，但是包含了重复元素。其实影响到的是，当左端点和右端点相等时，无法判断mid在左半边有序数组还是右半边有序数组，
所以只需要一直pop直到左端点和右端点不相等就可以了。就加上两句话即可：

"""
#大神做法1
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ######## 就是这两句 #######
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        ##########################
        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[0] <= nums[mid]:  # mid在左半边有序数组
                if nums[0] <= target < nums[mid]:  # 并且目标在左半边有序数组中
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # mid在右半边有序数组
                if nums[mid] < target <= nums[-1]:  # 并且目标在右半边有序数组中
                    left = mid + 1
                else:
                    right = mid - 1
        return False
