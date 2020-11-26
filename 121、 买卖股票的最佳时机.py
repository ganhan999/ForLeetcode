"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），
设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
 
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


"""

"""
思路分析：
从第一天开始遍历，如果后一天与当前最小值的差值大于最大差值，那么就记录该差值，否则保持不变。
记得要随时改变最小值。
"""
#我的做法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minval=prices[0]
        maxans=0
        for p in prices:
            minval=min(minval,p)
            maxans=max(maxans,p-minval)
        return maxans

#我的做法2

"""
动态规划
dp[i] 表示前 ii 天的最大利润，因为我们始终要使利润最大化，则：
dp[i] = max(dp[i-1], prices[i]-minprice)


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0  # 边界条件
        dp = [0] * n
        minprice = prices[0]
        for i in range(1,n):
            minprice=min(prices[i],minprice)
            dp[i]=max(dp[i-1],prices[i]-minprice)
        return dp[-1]

