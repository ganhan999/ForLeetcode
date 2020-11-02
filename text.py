from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        ss1= list(map(set, zip(strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

y=Solution()

zipped = list(zip(*["abba", "abaaa",'abcaa']))
print(zipped)
print(y.longestCommonPrefix(["abba", "abaaa",'abcaa']))

