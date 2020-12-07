from typing import List
from collections import deque
# import math
import codecs


class Solution:
    def reverseBits(self, n: int) -> int:
        a=list(bin(n))[2:]
        num=32-len(a)
        a.reverse()
        b="".join(a)+'0'*num
        return int(b,base=2)

print(Solution().reverseBits(43261596))