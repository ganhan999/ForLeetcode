from typing import List
from collections import deque
# import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def recursion(dividend, divisor):
            if dividend < divisor:
                return 0
            if dividend == divisor:
                return 1
            nn = 1
            dd = divisor
            while True:
                if dividend > dd:
                    n = nn
                    nn += nn
                    d = dd
                    dd += dd
                elif dividend == dd:
                    return nn
                else:
                    return n + recursion(dividend - d, divisor)

        if dividend >= 0:
            if divisor > 0:
                positive = True
            else:
                positive = False
        else:
            if divisor > 0:
                positive = False
            else:
                positive = True
        ans = recursion(abs(dividend), abs(divisor))
        if positive:
            if ans > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return ans
        else:
            return -ans





print(Solution().divide(20,3))