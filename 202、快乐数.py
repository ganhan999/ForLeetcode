"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。



示例 1：
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

示例 2：
输入：n = 2
输出：false


"""


"""
根据我们的探索，我们猜测会有以下三种可能。

1、最终会得到 11。
2、最终会进入循环。
3、值会越来越大，最后接近无穷大。
第三种情况不可能发生

所以只需要判断是否进入了循环
"""
#大神做法1
class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):#算下一个数
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:#如果是1就是快乐数，如果存在了那么就是遇到了循环就不是快乐数
            seen.add(n)
            n = get_next(n)

        return n == 1




"""
快慢指针判断循环
"""

#大神做法2
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1



"""
cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}   循环链只有这一条
"""
#大神做法3
class Solution:
    def isHappy(self, n: int) -> bool:

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1

