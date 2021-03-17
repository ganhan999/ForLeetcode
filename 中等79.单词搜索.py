"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
通过次数134,541提交次数305,651


"""


"""
回溯
"""
#大神做法1
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]
        def dfs(x, y, idx):
            """搜索单词
            Args:
                x: 行索引
                y: 列索引
                idx: 单词对应的字母索引
            """
            if board[x][y] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            # 先标记
            visited[x][y] = True
            # 找到符合的字母时开始向四个方向扩散搜索
            for i in range(4):
                nx = x + rows[i]
                ny = y + cols[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and dfs(nx, ny, idx + 1):#判断下一个字母是否匹配后面的字符串
                    return True
            # 扩散未搜索对应的字母，释放标记
            # 继续往其他方位搜索
            visited[x][y] = False#后面四个方向完全匹配不到就返回False，且把该元素置为False，相当于回溯
            return False
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


