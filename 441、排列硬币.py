"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

"""


"""
1.二分查找，设立左右边界分别为0和n，每次取中间值mid为行数，将mid行总数和n对比
2.和n相等时直接return mid，小于n时，左边界left=mid+1 ，大于n时，右边界right = mid-1
3.在不断的判定后如果硬币不能刚好分完，那么left会等于能分的最多行数+1，right会等于总量超出n的最小行数-1，即为能分的最多行数，return right

"""
#大神做法1
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while(True):
            if left>right:
                return right
            mid = (left+right)//2
            count = (1+mid)*mid/2
            if count == n:
                return mid
            elif count<n:
                left = mid+1
            else:
                right = mid-1



"""
用求和公式反解得到x的表达式 x = ((1+8*n)**0.5 - 1)/2
x后面的小数表示不完整的行，因此向下取整
"""
#大神做法2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        import math
        # 高斯求和，求根公式
        return math.floor(((1+8*n)**0.5 - 1)/2)



