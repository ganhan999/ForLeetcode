"""
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:
给定 nums = [3,2,2,3], val = 3,
函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。

示例2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2,
函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。


"""

"""
思路分析：
如果val在列表中，那么就使用index函数得到他的位置，然后再进行一个一个的pop，比较简单
"""
#我的做法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lens=len(nums)
        i=0
        if lens==0:
            return 0
        while i<=lens-1:
            if val in nums:
                inde=nums.index(val)
                nums.pop(inde)
                print()
            else:
                i=i+1
        return len(nums)



#大神做法1

"""
先计算出列表中有多少个val，然后进行循环删除便可。
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

#大神做法2

"""
双指针其实就是两个数，分别代表两个index，表示数组中第几个数的意思。
比如这里，我们让a代表一个index，b代表一个index
然后我们让a一直往后移动，相当于nums[a]从数组第一个数遍历到最后一个数。
当且仅当我们发现nums[a] != val的时候，我们把这个数拷贝到b指向的位置，
默认b是从0开始的，然后b += 1指向下一个位置。

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b



