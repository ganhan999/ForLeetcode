"""罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。
"""

"""
本题思路：
这题懂了就非常简单。首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，
如果当前字符代表的值不小于其右边，就加上该值；否则就减去该值。
以此类推到最左边的数，最终得到的结果即是答案
"""

#我的做法
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,"0":0}
        lens = len(s)
        print('lens=',lens)
        sum = 0
        s=s+"0"
        print(s)
        if lens == 1:
            return sum + a[s[0]]
        for i in range(lens):
            if a[s[i]] < a[s[i+1]] :
                sum = sum - a[s[i]]#前面比后面大 就取负数
            else :
                sum=sum+a[s[i]]
        return sum

#大神做法
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lens = len(s)
        print('lens=',lens)
        sum = 0
        for i in range(lens):
            if i<lens-1 and a[s[i]] < a[s[i+1]]:#把i<lens-1放前面，可以导致后面的断路！
                sum = sum - a[s[i]]
            else :
                sum=sum+a[s[i]]
        return sum