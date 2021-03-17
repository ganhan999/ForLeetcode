"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

"""

"""
思路分析：
因为是有序序列，只需要前一个与后一个比较即可，并不麻烦
"""
#我的做法
# Definition for singly-linked list.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        else:
            while(i<len(nums)-1):
                if nums[i]==nums[i+1]:
                    nums.pop(i)
                else:
                    i=i+1
        return len(nums)



#大神做法

"""
双指针法：题意可以理解为直接修改前k个数，因此无需删除操作
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[b] == nums[a]:
                b += 1
            else:
                a += 1
                nums[a] = nums[b]
        return a+1



"""


python中关于删除list中的某个元素，一般有三种方法:remove、pop、del：

1.remove: 删除单个元素，删除首个符合条件的元素，按值删除
举例说明:

>>> str=[1,2,3,4,5,2,6]
>>> str.remove(2)
>>> str
[1, 3, 4, 5, 2, 6]

 

2.pop: 删除单个或多个元素，按位删除(根据索引删除)

>>> str=[0,1,2,3,4,5,6]
>>> str.pop(1) #pop删除时会返回被删除的元素
>>> str
[0, 2, 3, 4, 5, 6]

 

>>> str2=['abc','bcd','dce']
>>> str2.pop(2)
'dce'
>>> str2
['abc', 'bcd']

 

3.del：它是根据索引(元素所在位置)来删除
举例说明:

>>> str=[1,2,3,4,5,2,6]
>>> del str[1]
>>> str
[1, 3, 4, 5, 2, 6]

 

>>> str2=['abc','bcd','dce']
>>> del str2[1]
>>> str2
['abc', 'dce']

 

除此之外，del还可以删除指定范围内的值。

>>> str=[0,1,2,3,4,5,6]
>>> del str[2:4] #删除从第2个元素开始，到第4个为止的元素(但是不包括尾部元素)
>>> str
[0, 1, 4, 5, 6]

 

del 也可以删除整个数据对象(列表、集合等)

>>> str=[0,1,2,3,4,5,6]
>>> del str
>>> str #删除后，找不到对象
"""