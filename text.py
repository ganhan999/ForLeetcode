from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            print(haystack.find(needle))
            return haystack.find(needle)
a=Solution()
print(a.strStr("hello","ll"))