from typing import List
from collections import deque
# import math
import re


from functools import reduce
class Solution:
    def singleNumber(nums):
        return reduce(lambda x, y: x ^ y, nums)

