"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。



"""

"""
思路分析：
这就是动态规划吗！爱了爱了！
先一步一步进行，为后一次做好准备。
基本思路就是遍历一遍，用两个变量，一个记录最大的和，一个记录当前的和。时空复杂度貌似还不错......
如图所示
https://leetcode-cn.com/problems/maximum-subarray/
solution/hua-jie-suan-fa-53-zui-da-zi-xu-he-by-guanpengchn/
"""
#我的做法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        ans=nums[0]#一开始就要给nums[0]，不然如果第一个数是负数就惨了
        for i in range(len(nums)-1):
            num=nums[i+1]
            if sum<=0:
                sum=num#小于零，就把前面的都不算
                ans=max(sum,ans)#看是之前大还是现在大
            else:
                sum=sum+num
                ans=max(sum,ans)#看是之前大还是现在大
        return ans

#大神做法1

"""
最简单的的动态规划！这才是最简单的！

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])#如果我前面加起来的值是一个正数，那么就继续加。
                                                    # 如果不是的话，抱歉我要从头开始了。
        return max(nums)


#大神做法2

"""
分治思想
如图所示
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        # 以下条件是只有n>1才会发生的
        #拆分为二叉树的形式，递归求出每一个子树的最大值。
        a=nums
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

