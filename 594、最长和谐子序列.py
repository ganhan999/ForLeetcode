"""

和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。



示例 1：
输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]

示例 2：
输入：nums = [1,2,3,4]
输出：2

示例 3：
输入：nums = [1,1,1,1]
输出：0



"""


"""
利用哈希表存储数组中元素出现的次数
遍历哈希表，如果当前元素+1也在哈希表中，那么计算两者次数之和，保留最大值
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dicts={}
        for i in nums:
            dicts[i]=dicts.get(i,0)+1
        res=0
        for i in dicts:
            if i+1 in dicts:
                res=max(res,dicts[i]+dicts[i+1])
        return res

"""
首先将原数组排序，得到递增数组；
然后遍历一遍数组，利用双指针实现类似滑动窗口的功能
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        res=0
        for right in range(len(nums)):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                res=max(res,right-left+1)
        return res

