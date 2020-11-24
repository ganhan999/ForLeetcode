"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

"""
思路分析：
在每一层加完后，左右加上元素1
"""
#我的做法
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==1:
            return [[1],[1,1]]
        li = [[1], [1, 1]]
        for i in range(3,numRows+1):
            new=[]
            for j in range(i-2):
                new.append(li[i-2][j]+li[i-2][j+1])
            new.insert(0, 1)
            new.append(1)
            li.append(new)
        return li

#大神做法

"""
先生成都是1的一列，再通过代替获得。
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res

