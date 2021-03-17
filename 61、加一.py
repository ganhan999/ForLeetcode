"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

"""
思路分析：
转成数字后，加一，再转字符串，注意特殊情况！
"""
#我的做法
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lens=len(digits)
        sum=0
        sumlist=[]
        for i in range(lens):
            sum=10**(lens-i-1)*digits[i]+sum#转为数字
        sum=sum+1
        strnum=str(sum)
        for i in range(len(strnum)):
            sumlist.append(int(strnum[i]))#再转字符串
        if lens-len(sumlist)==-1 or lens-len(sumlist)==0:#如果出现0，0，9变0，1，0的情况判断是否前面是不是有多余的0.
            return sumlist
        else:
            anum=lens-len(sumlist)
            for i in range(anum):
                sumlist.insert(0,0)
        return sumlist

#大神做法1

"""
从倒数第一个数字开始，如果数字为9，那么置为0，判断前一个如果不是9，那么就只要加上1就结束了！！
如果是9呢，那么就继续置为0，以此类推。如果到第一个数字都还是9，那么置为0后，我们需要插入一个1。
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i] += 1
                return digits
            else:
                digits[i] =0
        digits.insert(0,1)
        return digits


'''
下面是join函数的介绍

Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
它只能用在字符串中！！！

语法
join()方法语法：

‘sep’.join（strseq）

strseq.join(sep)

sep：分隔符，可以为空

strseq：字符串






下面是map函数的介绍

map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法
map() 函数语法：

map(function, iterable, ...)

>>>def square(x) :            # 计算平方数
...     return x ** 2

>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]

'''