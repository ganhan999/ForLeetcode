from typing import List
from collections import deque
# import math


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                dfs(index+1 ,  path + [candidates[index]], residue - candidates[index])#这里index+1是为了每个元素只出现一次

        size = len(candidates)
        if size == 0:
            return []
        path = []
        candidates.sort()
        res = []
        dfs(0, path, target)
        return res



print(Solution().combinationSum2([10,1,2,7,6,1,5],8))