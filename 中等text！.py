import collections
from typing import List
from collections import deque
# import math


from typing import List

from typing import List


class Solution:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            c=1
            counts = [0] * 26
            for cc in st:
                c *= Solution.prime[ord(cc)-97]
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[c].append(st)
        return list(mp.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

