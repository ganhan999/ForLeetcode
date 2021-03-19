"""
给定两个字符串形式的非负整数num1 和num2，计算它们的和。



提示：

num1 和num2的长度都小于 5100
num1 和num2 都只包含数字0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式



"""


"""
利用int函数
"""
#大神做法1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


"""
标准加法进位，主要理解一下ASCII转换。
"""
#大神做法2
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            n1 = num1[i] if i >= 0 else '0'
            n2 = num2[j] if j >= 0 else '0'
            temp = ord(n1) + ord(n2) - 2 * ord('0') + carry
            cur = temp % 10
            carry = temp // 10
            res = chr(cur + 48) + res
            i -= 1
            j -= 1
        return '1' + res if carry != 0 else res



