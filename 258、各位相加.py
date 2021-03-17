"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:
输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于2 是一位数，所以返回 2。





"""


"""

x*100+y*10+z=x*99+y*9+x+y+z

"""
#大神做法1
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num!=0 else 0





