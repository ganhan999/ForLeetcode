"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如 sqrt。

示例 1：
输入：16
输出：True

示例 2：
输入：14
输出：False




"""

"""
二分法
"""
#大神做法1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l < r:
            mid = (l + r) // 2
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid
        return l * l == num


"""
牛顿迭代法

"""
#大神做法1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


