"""
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""


"""
反证法，假设不存在有一个值是重复两次的，那么列表和集合的个数应该相同
"""
#我的做法
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len1=len(nums)
        set1=set(nums)
        len2=len(set1)
        return True if len1!=len2 else False



#大神做法1
"""
排序后，然后判断前后元素是否相等
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 先对数组排序
        nums.sort()
        # 遍历数组，比较前后元素值
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False





