"""
实现int sqrt(int x)函数。
计算并返回x的平方根，其中x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
    由于返回类型是整数，小数部分将被舍去。

"""

"""
思路分析：
二分法就完事了，比较简单（但是我一开始还是想穷举法，笨啊！）
"""
#我的做法
class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        while low<=high:
            mid=(low+high)//2
            if mid**2<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans


#大神做法1

"""
√x=e的1/2lnx次方（有点蠢）

"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans



