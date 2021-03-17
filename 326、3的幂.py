"""
给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x


示例 1：
输入：n = 27
输出：true

示例 2：
输入：n = 0
输出：false

示例 3：
输入：n = 9
输出：true

示例 4：
输入：n = 45
输出：false




"""


"""
暴力迭代
"""
#大神做法1
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while True:
            if n == 1:
                return True
            elif n%3 == 0:
                n = n/3
            else:
                return False


"""
我们只需要将 3^{9 除以 n。若余数为 0 意味着 n 是 3^19的除数，因此是3的幂。
"""
#大神做法2
class Solution:
    def isPowerOfThree1(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

