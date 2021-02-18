"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 20 = 1

示例 2:
输入: 16
输出: true
解释: 24 = 16

示例 3:
输入: 218
输出: false


"""


"""
一直除二，除到是奇数或者为1为止
"""
#大神做法1
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1



"""
恒有 n & (n - 1) == 0和n>0的条件就是二的幂
这里n二进制最高位为1，其他为0
n-1则相反
"""
#大神做法2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


"""
数1的个数
"""
#大神做法3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>=0 and bin(n).count('1') == 1

