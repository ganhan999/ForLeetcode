from typing import List
from collections import deque
# import math
import codecs


def trailingZeroes(self, n: int) -> int:
    n_factorial = 1
    for i in range(2, n + 1):
      n_factorial *= i
    zero_count = 0
    while n_factorial % 10 == 0:
      zero_count += 1
      n_factorial //= 10

    return zero_count



print(Solution().titleToNumber("ZZY"))