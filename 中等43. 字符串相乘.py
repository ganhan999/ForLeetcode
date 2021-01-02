"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

"""

"""
做加法，小学竖列式
"""

#大神做法1
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)

        return ans

    def addStrings(self, num1: str, num2: str) -> str:#字符串累加
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])


"""
做乘法
"""

#大神做法2
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 先将字符串倒序
        from collections import deque
        dq_1 = deque(num1)
        dq_2 = deque(num2)

        dq_1.reverse()
        dq_2.reverse()

        num1 = "".join(dq_1)
        num2 = "".join(dq_2)

        # 根据长度按数字的位数来恢复数值
        l1 = len(num1)
        l2 = len(num2)

        number1 = 0
        number2 = 0

        for i, j in zip(num1, range(l1)):#假设num1=“123",zip(num1, range(l1))等于[(1, 0), (2, 1), (3, 2)]
            number1 += int(i) * 10 ** j

        for i, j in zip(num2, range(l2)):
            number2 += int(i) * 10 ** j

        return str(number1 * number2)
