"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2


"""

"""
题干中说明不能用乘法和除法, 那么我们可以用减法, 被除数最多可以减多少个除数还能保证是非负的即可.

"""
#大神做法1
class Solution:
    def divide(self, dividend, divisor):
        sig = True if dividend*divisor > 0 else False  # 判断二者相除是正or负
        dividend, divisor= abs(dividend), abs(divisor)  # 将被除数和除数都变成正数
        count = 0  # 用来表示减去了多少个除数，也就是商为多少
        while divisor <= dividend:  # 当被除数小于除数的时候终止循环
            dividend -= divisor
            count += 1
        res = count if sig == True else -count  # 给结果加上符号
        return max(min(res, 2**31-1), -2**31)





#大神做法2

"""
比如 divide(20, 3)：

先将3不断翻倍，知道超过20，翻1次为2倍得6，翻2次为4倍得12，翻3次为8倍的24
这时4倍12是我们需要的值
递归 4 + divide(20-12, 3)
递归出口为：被除数 < 除数时返回0， 被除数 == 除数时返回1
需要额外处理被除数和除数不同号

用翻倍的形式减少时间
"""


class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		def recursion(dividend, divisor):
			if dividend < divisor:
				return 0
			if dividend == divisor:
				return 1
			nn = 1
			dd = divisor
			while True:
				if dividend > dd:
					n = nn
					nn += nn
					d = dd
					dd += dd#翻倍
				elif dividend == dd:
					return nn
				else:
					return n + recursion(dividend - d, divisor)

		if dividend >= 0:
			if divisor > 0:
				positive = True
			else:
				positive = False
		else:
			if divisor > 0:
				positive = False
			else:
				positive = True
		ans = recursion(abs(dividend), abs(divisor))
		if positive:
			if ans > 2 ** 31 - 1:
				return 2 ** 31 - 1
			else:
				return ans
		else:
			return -ans


