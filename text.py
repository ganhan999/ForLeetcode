from typing import List
from collections import deque
# import math
import codecs


class Solution1:
  def convertToTitle2(self, n: int) -> str:
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n -= 1
    if n < 26:
      return eng[n]
    return self.convertToTitle2(n // 26) + eng[n % 26]

2
print(Solution1().convertToTitle2(26))