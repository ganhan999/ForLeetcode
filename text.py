from typing import List
from collections import deque
# import math
import codecs


class Solution(object):
  def titleToNumber(self, s):
    ans = 0
    for x in s:
      ans *= 26
      ans += ord(x) - ord('A') + 1
    return ans
print(Solution().titleToNumber("ZZY"))