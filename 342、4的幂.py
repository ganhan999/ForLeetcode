"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x


示例 1：
输入：n = 16
输出：true

示例 2：
输入：n = 5
输出：false

示例 3：
输入：n = 1
输出：true




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
            elif n%4 == 0:
                n = n/4
            else:
                return False


"""
预先计算所有可能的值
然后比对是不是在可能的集合里面
"""
#大神做法2
class Powers:
    def __init__(self):
        max_power = 15
        self.nums = nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i - 1]

class Solution:
    p = Powers()
    def isPowerOfFour(self, num: int) -> bool:
        return num in self.p.nums


"""
如果数字为 4 的幂 x = 4^a 那么a=1/2 log2 x，那么只要判断log2 x是偶数即可
"""
#大神做法3
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0


"""
位运算 
先利用num > 0 and num & (num - 1) == 0 判断是不是2的幂次
然后再即 4^a &(101010...10) == 0判断是不是4次幂
"""
#大神做法4
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0



"""
位运算2 
先利用num > 0 and num & (num - 1) == 0 判断是不是2的幂次
然后再即 num % 3 == 1判断是不是4次幂
"""
#大神做法5
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1
