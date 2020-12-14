from typing import List
from collections import deque
# import math
import codecs

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                res=max(res,(j-i)*min(height[i],height[j]))
        return res



print(Solution().myAtoi("+1"))