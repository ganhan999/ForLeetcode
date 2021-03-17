"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），
返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，
并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的示例 3中，输入表示有符号整数 -3。

进阶：
如果多次调用这个函数，你将如何优化你的算法？

示例 1：
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011中，共有三位为 '1'。

示例 2：
输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000中，共有一位为 '1'。

示例 3：
输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。


"""


"""
库函数
"""
#大神做法1
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")



"""
每次都与1相与，然后将原字符串右移一位
"""

#大神做法2
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n&1
            n>>=1
        return res



"""
n&(n-1)会消掉最低位的1，看一共能消除多少次，就有多少个1
"""
#大神做法3
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n&1
            n>>=1
        return res
