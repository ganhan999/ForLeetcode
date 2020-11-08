"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置

你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0



"""

"""
思路分析：
利用python中index函数便可以直接找到，子字符串的初始位置。
"""
#我的做法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort(reverse=False)
            return nums.index(target)


#大神做法1

"""
因为有序，所以只需要比较比它小的数的最大值
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([i for i in nums if i < target])




#大神做法2

"""
传统二分查找法
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        while(low<high):
            mid=low+(high-low)//2# “ / ” 为浮点数除法，返回浮点结果
                                 # “ // ” 表示整数除法，返回不大于结果的一个最大整数
            if nums[mid] > target:
                high=mid
            elif nums[mid]<target:
                low=mid+1
            else:
                return mid
        return low
"""


Python如何对列表排序？
Python list内置sort()方法用来排序，也可以用python内置的全局sorted()方法来对可迭代的序列排序生成新的序列。

1）排序基础

简单的升序排序是非常容易的。只需要调用sorted()方法。它返回一个新的list，新的list的元素基于小于运算符(__lt__)来排序。

>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
你也可以使用list.sort()方法来排序，此时list本身将被修改。通常此方法不如sorted()方便，但是如果你不需要保留原来的list，此方法将更有效。

>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
另一个不同就是list.sort()方法仅被定义在list中，相反地sorted()方法对所有的可迭代序列都有效。

>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

2）key参数/函数

从python2.4开始，list.sort()和sorted()函数增加了key参数来指定一个函数，此函数将在每个元素比较前被调用。 例如通过key指定的函数来忽略字符串的大小写：

>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。这个技术是快速的因为key指定的函数将准确地对每个元素调用。

更广泛的使用情况是用复杂对象的某些值来对复杂对象的序列排序，例如：

复制代码
>>> student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]








Python如何在列表中增加元素？

1. append() 追加单个元素到List的尾部，只接受一个参数，参数可以是任何数据类型，被追加的元素在List中保持着原结构类型。

此元素如果是一个list，那么这个list将作为一个整体进行追加，注意append()和extend()的区别。

复制代码代码如下:

>>> list1=['a','b']
>>> list1.append('c')
>>> list1
['a', 'b', 'c']


2. extend() 将一个列表中每个元素分别添加到另一个列表中，只接受一个参数；extend()相当于是将list B 连接到list A上。

复制代码代码如下:

>>> list1
['a', 'b', 'c']
>>> list1.extend('d')
>>> list1
['a', 'b', 'c', 'd']


3. insert() 将一个元素插入到列表中，但其参数有两个（如insert(1,”g”)），第一个参数是索引点，即插入的位置，第二个参数是插入的元素。

复制代码代码如下:

>>> list1
['a', 'b', 'c', 'd']
>>> list1.insert(1,'x')
>>> list1
['a', 'x', 'b', 'c', 'd']

4. + 加号，将两个list相加，会返回到一个新的list对象，注意与前三种的区别。前面三种方法（append, extend, insert）可对列表增加元素的操作，他们没有返回值，是直接修改了原数据对象。 注意：将两个list相加，需要创建新的list对象，从而需要消耗额外的内存，特别是当list较大时，尽量不要使用“+”来添加list，而应该尽可能使用List的append()方法。

复制代码代码如下:

>>> list1
['a', 'x', 'b', 'c', 'd']
>>> list2=['y','z']
>>> list3=list1+list2
>>> list3
['a', 'x', 'b', 'c', 'd', 'y', 'z']


"""