import collections
from typing import List
from collections import deque
# import math


from typing import List

from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 一维dp
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]



print(Solution().uniquePaths(3,5))
