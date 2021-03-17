"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
输入: 3
输出: 0
解释:3! = 6, 尾数中没有零。

示例2:
输入: 5
输出: 1
解释:5! = 120, 尾数中有 1 个零.


"""


"""
先计算阶乘，在计算尾数有多少个0
"""
#我的做法
class Solution:
    def trailingZeroes(self, n: int) -> int:
       n_factorial = 1
       for i in range(2, n + 1):
            n_factorial *= i
       zero_count = 0
       while n_factorial % 10 == 0:
           zero_count += 1
           n_factorial //= 10
       return zero_count


#大神做法1

"""
例如，如果 n=16，我们需要查看 1 到 16 之间所有数字的因子。
我们只对 2 和 5 有兴趣。包含 55 因子的数字是 {5，10，15}
包含因子 2 的数字是 {2、4、6、8、10、12、14、16}
因为只三个完整的对，因此 16! 后有三个零。
首先，我们可以注意到因子 2 数总是比因子 5 大。
为什么？因为每四个数字算作额外的因子 2，
但是只有每 25 个数字算作额外的因子 5。
因此我们可以删除计算因子 2 的过程
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        for i in range(5, n + 1, 5):
            current = i
            while current % 5 == 0:
              zero_count += 1
              current //= 5

        return zero_count



#大神做法2

"""
根据大神做法1，把除以25、除以125、除以625……不能大于n的个数都算出来，相加就行。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        current_multiple = 5
        while n >= current_multiple:
            zero_count += n // current_multiple
            current_multiple *= 5
        return zero_count
