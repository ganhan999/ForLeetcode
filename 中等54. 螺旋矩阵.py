"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


"""
利用余数作为改方向的手段，并且遍历的顺序是右下左上，
dx = [0, 1, 0, -1]  # 方向：右，下，左，上
dy = [1, 0, -1, 0]  # 注：与通常平面坐标系 记号 不同
到了尽头了就变一次
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        x = y = 0  # 矩阵元素位置初始化
        res = []  # 初始化，存储遍历后的矩阵元素
        dx = [0, 1, 0, -1]  # 方向：右，下，左，上
        dy = [1, 0, -1, 0]  # 注：与通常平面坐标系 记号 不同
        di = 0  # 初始化方向变量
        visited = set()  # 初始化集合，存储已走过的坐标
        m, n = len(matrix), len(matrix[0])  # 矩阵的行列

        for i in range(m * n):  #
            res.append(matrix[x][y])  # 存储遍历矩阵过的元素
            visited.add((x, y))  # 存储遍历过的坐标
            tx, ty = x + dx[di], y + dy[di]  # 先记录下一步坐标，用于判断下一步怎么走
            if 0 <= tx < m and 0 <= ty < n and (tx, ty) not in visited:  # 判断坐标是否需变向，且没有遍历过
                x, y = tx, ty
            else:
                di = (di + 1) % 4  # 改变方向，右下左上为一圈，防止方向坐标越界
                x, y = x + dx[di], y + dy[di]  # 下一步坐标
        return res





"""
可以将矩阵看成若干层，首先输出最外层的元素，其次输出次外层的元素，直到输出最内层的元素。
定义矩阵的第 k 层是到最近边界距离为 k 的所有顶点。
例如，下图矩阵最外层元素都是第 1 层，次外层元素都是第 2 层，剩下的元素都是第 3 层。


"""
#大神做法2
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

"""
利用zip函数，每次都把那一行或者那一列pop出来，然后用zip函数生成新的矩阵
太妙了
"""
#大神做法3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res