"""
给定一个正整数n，生成一个包含 1 到n2所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


"""


"""
利用余数作为改方向的手段，并且遍历的顺序是右下左上，
dx = [0, 1, 0, -1]  # 方向：右，下，左，上
dy = [1, 0, -1, 0]  # 注：与通常平面坐标系 记号 不同
到了尽头了就变一次
"""

#大神做法1
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        list0 = [j for j in range(1,n**2 + 1)]                          # 生成长列表
        x = y = 0
        dx = [0,1,0,-1]                                                 # 方向坐标
        dy = [1,0,-1,0]
        di = 0
        visited = set()                                                 # 初始化集合，用于记录已走过坐标
        list1 = [[None for k in range(n)] for k in range(n)]            # 生成空矩阵
        for i in range(n**2):
            list1[x][y] = list0[i]
            visited.add((x,y))
            nx,ny = x + dx[di],y+dy[di]                                 # 记录下一步操作
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited:          # 判断是否越界，未曾走过的路
                x,y = nx,ny
            else:
                di = (di+1)%4
                x,y= x+dx[di],y+dy[di]
        return list1





"""
从外到内
"""
#大神做法2
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat