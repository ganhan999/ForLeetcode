"""
给定一个非空整数数组，除了某个元素只出现一次以外，
其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例2:
输入: [4,1,2,1,2]
输出: 4
"""


"""
先排序，然后相同元素则会相邻。循环一次判断前一个元素是否等于后一个元素，
间隔一个判断一个即可，如果不相等就是想要的结果。
"""
#我的做法
class Solution:
    def singleNumber(nums):
        if len(nums)==1:   #如果数组长度为1，则直接返回即可
            return nums[0]
        nums.sort()     #对数组进行排序，使其相同元素靠在一起
        for i in range(1,len(nums),2):   #循环数组，验证前后是否相同，由于原始出现两次，因此可跳跃判断
            if nums[i-1] != nums[i]:
                return nums[i-1]
            if (i+2) == len(nums):   #判断单一元素在排序后数组的最后面
                return nums[-1]

#大神做法1

"""
由于目标元素只有一次，其他元素有多次，
因此，依次删除列表的元素，同一个元素删除两次，报错则为目标值。
"""
class Solution:
    def singleNumber(nums):
        while True:
            d = nums[0]
            nums.remove(d)
            try:
                nums.remove(d)
            except:
                return d

#大神做法2

"""
方法三：一个元素出现一次、其他出现多次，那么数组求和，与去重后的和相差的就是目标值。
"""
class Solution:
    def singleNumber(nums):
        return sum(set(nums))*2-sum(nums)


#大神做法3
"""
0和任何数异或的结果都是这个数本身。
相同的数异或的结果为0。
这个数列里面除了一个数只出现了一次，其他数都出现了两次。
异或运算满足交换律和结合律。
因此从前往后依次异或即可。最终结果就是那个只出现一次的数。
比如 1 xor 1 xor 2 xor 3 xor 2 = (1 xor 1) xor (2 xor 2) xor 3 = 0 xor 0 xor 3 = 0 xor 3 = 3
"""
from functools import reduce
class Solution:
    def singleNumber(nums):
        return reduce(lambda x, y: x ^ y, nums)




"""
下面是 reduce函数介绍
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

注意：Python3.x reduce() 已经被移到 functools 模块里，
如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：

from functools import reduce


from functools import reduce

def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数


"""