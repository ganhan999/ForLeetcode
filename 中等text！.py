from typing import List
from collections import deque
# import math
import codecs

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ans=""
        n=len(s)
        for i in range(numRows):
            k=i
            while k<n:
                ans+=s[k]
                k+=2*(numRows-1)
                if i!=0 and i!=numRows-1 and k-2*i <n:
                    ans+=s[k-2*i]
        return ans


print(Solution().convert("PAYPALISHIRING",3))