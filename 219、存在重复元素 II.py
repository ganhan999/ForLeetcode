"""
给定一个整数数组和一个整数k，判断数组中是否存在两个不同的索引i和j，
使得nums [i] = nums [j]，并且 i 和 j的差的 绝对值 至多为 k。


示例1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false


"""


"""
哈希表 
键为数字，值为下标
"""
#大神做法1
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 创建哈希表
        hash_map = {}
        # 遍历一次数组
        for idx, n in enumerate(nums):
            if n not in hash_map or (idx - hash_map[n]) > k:  # 情况1 & 情况2
                hash_map[n] = idx
            else:  # 情况3
                return True
        else:
            return False