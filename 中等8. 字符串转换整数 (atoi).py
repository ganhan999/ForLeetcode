"""
请你来实现一个atoi函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

示例 1:
输入: "42"
输出: 42

示例2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
    我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。

示例5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
    因此返回 INT_MIN (−231) 。


"""



"""
遍历每一个元素，判断是不是正负号或者数字
"""
#我的做法1


class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0
        state=1
        flag=0
        s1=""
        for i in s:
            if flag==0:
                if i=="-":
                    s1+=i
                    flag=1
                elif i=="+":
                    s1 += i
                    flag=1
                elif i.isnumeric():
                    s1 += i
                    flag=1
                elif i.isspace():
                    continue
                else:
                    return 0
            else:
                if i.isnumeric():
                    s1 += i
                else:
                    break
        if flag==0:
            return 0
        if s1[0]=="-":
            state=0
            s1=s1[1:]
        elif s1[0] == "+":
            s1=s1[1:]
        s1=self.atoi(s1)
        if state==0:
            s1=-s1
        if s1>=-2 ** 31 and s1<=(2 ** 31) - 1:
            return s1
        elif s1<-2 ** 31:
            return  -2 ** 31
        else:
            return  (2 ** 31) - 1
    def atoi(self,s):
        s = s[::-1]
        num = 0
        for i, v in enumerate(s):
            offset = ord(v) - ord('0')
            num += offset * (10 ** i)
        return num


#大神做法1

"""
正则表达式

"""

class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        mathes=re.match('[ ]*([+-]?\d+)',str)
        if not mathes:
            return 0
        ans=int(mathes.group(1))
        return min(max(ans,-2**31),2**31-1)

