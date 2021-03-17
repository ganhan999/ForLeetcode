"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
格雷编码序列必须以 0 开头。


示例 1:
输入:2
输出:[0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的n，其格雷编码序列并不唯一。
例如，[0,2,3,1]也是一个有效的格雷编码序列。
00 - 0
10 - 2
11 - 3
01 - 1

示例2:
输入:0
输出:[0]
解释: 我们定义格雷编码序列必须以 0 开头。
    给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
    因此，当 n = 0 时，其格雷编码序列为 [0]。

"""


"""
看官方文档
https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/
"""
#大神做法1
class Solution:
    def grayCode(self, n: int) -> List[int]:
        '''
        格雷编码结论：
        设G(n)表示总位数为n的各类编码集合，根据以下策略可以求出G(n+1)
        1. 将G(n)的每个元素前添加0得到G'(n)
        2. 将G'(n)反转得到镜像R(n)，在R(n)中的每个元素前添加1得到R'(n)
        3. 将G'(n)与R'(n)合并得到G(n+1)

        编码思路：
        1. 初始化G(0)和位数标识head
        2. 外层循环次数为总位数n
        3. 内层循环倒序遍历res(对应上述第2步反转),位数标识加上当前索引对应的值即为R'(n)中的元素
        4. 在res后追加上述计算的元素，遍历结束，得到Gray编码集
        '''
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res)-1, -1, -1):
                res.append(head+res[j])#这里就相当于在最前面加了一个1，前面的不变，后面加一倍
            head <<= 1
        return res