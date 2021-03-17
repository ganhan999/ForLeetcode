"""
给定一个m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例1:
输入:
[
 [1,1,1],
 [1,0,1],
 [1,1,1]
]
输出:
[
 [1,0,1],
 [0,0,0],
 [1,0,1]
]

示例2:
输入:
[
 [0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]
]
输出:
[
 [0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]
]
进阶:
一个直接的解决方案是使用 O(mn)的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m+n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？


"""


"""
我们扫描一遍原始矩阵，找到所有为零的元素。
如果我们找到 [i, j] 的元素值为零，我们需要记录下行号 i 和列号 j。
用两个 sets ，一个记录行信息一个记录列信息。
最后，我们迭代原始矩阵，对于每个格子检查行 r 和列 c 是否被标记过，如果是就将矩阵格子的值设为 0。

时间复杂度：O(M×N)，其中 M 和 N 分别对应行数和列数。
空间复杂度：O(M+N)。
"""
#大神做法1
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0




"""
遍历原始矩阵，如果发现如果某个元素 cell[i][j] 为 0，我们将第 i 行和第 j 列的所有非零元素设成很大的负虚拟值（比如说 -1000000）。注意，正确的虚拟值取值依赖于问题的约束，任何允许值范围外的数字都可以作为虚拟之。
最后，我们便利整个矩阵将所有等于虚拟值（常量在代码中初始化为 MODIFIED）的元素设为 0。

"""
#大神做法2
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the non zeros to MODIFIED
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
        for r in range(R):
            for c in range(C):
                # Make a second pass and change all MODIFIED elements to 0 """
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0




"""
遍历整个矩阵，如果 cell[i][j] == 0 就将第 i 行和第 j 列的第一个元素标记。
第一行和第一列的标记是相同的，都是 cell[0][0]，所以需要一个额外的变量告知第一列是否被标记，
同时用 cell[0][0] 继续表示第一行的标记。
然后，从第二行第二列的元素开始遍历，如果第 r 行或者第 c 列被标记了，那么就将 cell[r][c] 设为 0。
这里第一行和第一列的作用就相当于方法一中的 row_set 和 column_set 。
然后我们检查是否 cell[0][0] == 0 ，如果是则赋值第一行的元素为零。
然后检查第一列是否被标记，如果是则赋值第一列的元素为零。

"""
#大神做法3
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0
