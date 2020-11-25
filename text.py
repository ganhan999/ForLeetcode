from typing import List
from collections import deque
# import math



class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        min_val =prices[0]
        res = 0
        for i in range(n):
            # 遍历数组，不断更新最小价格
            # 再计算出max(当前值-最小值)
            if min_val>=prices[i]:
                min_val = prices[i]
            tmp = prices[i]-min_val
            if tmp>res:
                res = tmp
        return res


print(Solution(). maxProfit([7,1,5,3,6,4]))

