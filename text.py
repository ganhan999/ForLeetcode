from typing import List
from collections import deque
# import math



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        if n == 0: return result
        for i in range(n-1):
            result+=max(prices[i+1]-prices[i],0)
        return result
print(Solution(). maxProfit([7,1,5,3,6,4]))

