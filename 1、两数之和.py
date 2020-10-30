
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""

#我的做法：
class Solution:
    def twoSum(self,nums,target):
        len1=len(nums)
        for i in range(len1):
            j=i+1
            for j in range(j,len1):
              if nums[i]+nums[j]==target:
                  return [i,j]
        return [0,0]


"""
大神做法：
参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。
用枚举的方式，构造哈希表
"""

class Solution:
    def twoSum(self,nums, target):
        hashmap={}
        for i,j in enumerate(nums):
            hashmap[j]=i
        for n,m in enumerate(nums):
            number=hashmap.get(target-m)
            if number is not None and n!=number:
                return[n,number]
        return[0,0]

#复现成功！
