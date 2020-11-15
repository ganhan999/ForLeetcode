"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

"""

"""
思路分析：
递归算法！（认真思考需要做执行操作）
注意缓存装饰器！

"""
#我的做法
class Solution:
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:


#大神做法1

"""
斐波那契数列算法
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        res = (((1+5**0.5)/2)**(n+1)-((1-5**0.5)/2)**(n+1))/((5)**0.5)
        return int(res)



#大神做法2

"""
动态规划算法1，只存储前两个元素，减少了空间，空间复杂度O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        f1,f2=1,2
        if n==1:
            return f1
        if n==2:
            return f2
        for i in range(n-2):
            f2,f1=f1+f2,f2
            print(f1,f2)
        return f2


#大神做法3

"""
动态规划算法2，新建一个字典或者数组来存储以前的变量，空间复杂度O(n)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

