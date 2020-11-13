"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
 
提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

"""

"""
思路分析：
先换成十进制然后换二进制，最后取一个[2:]，注意bin（）后返回的是一个字符串
"""
#我的做法
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        anum=int(a,base=2)
        bnum=int(b,base=2)
        return (bin(anum+bnum)[2:])


#大神做法1

"""
非内置函数
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):#这里是对二进制的掌握程度
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return '1' + r if p else r#如果最后p还是进位了，那么就往前面加1，否则就不加！

