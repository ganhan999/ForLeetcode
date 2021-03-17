"""
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右


"""


"""
动态规划，每一个格子都是左边或者上面格子的总和，边界条件都是1，一维和二维数组的空间利用率不同
"""

#大神做法1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 一维dp
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]#dp[j - 1]左边的数值，dp[j]上一层的数值
        return dp[-1]

"""
排列组合，数学公式
"""
#大神做法2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

