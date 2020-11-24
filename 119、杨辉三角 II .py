"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

示例:
输入: 3
输出: [1,3,3,1]
"""

"""
思路分析：
判断i是不是这一层，再输出
"""
#我的做法
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        li = [[1], [1, 1]]
        i = 3
        while True:
            new = []
            for j in range(i - 2):
                new.append(li[i - 2][j] + li[i - 2][j + 1])
            new.insert(0, 1)
            new.append(1)
            li.append(new)
            if rowIndex == i - 1:
                return li[i - 1]
            i = i + 1

#我的做法2

"""
判断i是不是这一层，再输出
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        i = 0
        while True:
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
            if rowIndex==i:
                return res[i]
            i=i+1


