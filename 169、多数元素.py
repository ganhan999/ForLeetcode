"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于⌊ n/2 ⌋的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。


示例1:

输入: [3,2,3]
输出: 3
示例2:

输入: [2,2,1,1,1,2,2]
输出: 2


"""


"""
排序之后，找最中间这个就行了
"""
#我的做法
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[(1+len(nums)//2)-1]


#大神做法1

"""
这就相当于每个“多数元素”和其他元素两两相互抵消，抵消到最后肯定还剩余至少1个“多数元素”。

无论数组是1 2 1 2 1，亦或是1 2 2 1 1，总能得到正确的候选人。


"""


class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        major = 0
        count = 0
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1
        return major





