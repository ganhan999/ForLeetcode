"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


"""


"""
回溯算法
"""
#大神做法1
class Solution:
    def combine(self, n: int, k: int) -> list:
        ans = list()

        def backtrack(tmp: list, index: int) -> None:
            if len(tmp) == k:
                ans.append(tmp[:])
                return
            for i in range(index, n + 1):
                tmp.append(i)
                backtrack(tmp, i + 1)
                tmp.pop()
        backtrack([], 1)
        return ans


"""
用Python的itertools来写组合组合
"""
#大神做法2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
         return list(itertools.combinations(range(1,n+1),k))
