"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2

"""


"""
参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。
用枚举的方式，构造哈希表
"""
#我的做法
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i,j in enumerate(numbers):
            hashmap[j]=i
        for n,m in enumerate(numbers):
            number=hashmap.get(target-m)
            if number is not None and n!=number:
                return[n+1,number+1]
#大神做法1

"""
二分查找
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            target1 = target - numbers[i]
            left , right = i+1 , len(numbers) - 1
            while left <= right:
                mid = (left+right)//2
                if target1 < numbers[mid]:
                    right = mid - 1
                elif target1 > numbers[mid]:
                    left = mid + 1
                else:
                    return [i+1,mid+1]




#大神做法2

"""
双指针分别指向最左和最右元素，如果两边之和大于target，那么右指针左移，否则左指针右移。
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0 , len(numbers)-1
        while left <= right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1,right+1]
            elif s < target:
                left += 1
            else:
                right -= 1




