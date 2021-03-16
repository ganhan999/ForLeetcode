"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用补码运算方法。

注意:
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

示例 1：
输入:
26
输出:
"1a"

示例 2：
输入:
-1
输出:
"ffffffff"


"""


"""
1、当正数时，直接循环右移4位（除以16也可以），直到商为0，再依次将余数字符串起来，逆序排列。
2、当0时，直接返回0。
3、当负数时，将其绝对值通过与（2的32次方减1）异或再加1，转化为对应的十进制正数，然后执第一步的操作。


"""
#大神做法1
class Solution:
    def toHex(self, num: int) -> str:
        stra = ''
        if num < 0:
            num = (abs(num) ^ ((2 ** 32) - 1)) + 1
        elif num == 0:
            return '0'
        while (num >> 4) > 0 or num > 0:
            a = str(num & 0xf)
            if a == '10': a = 'a'
            elif a == '11': a = 'b'
            elif a == '12': a = 'c'
            elif a == '13': a = 'd'
            elif a == '14': a = 'e'
            elif a == '15': a = 'f'
            stra += a
            num = num >> 4
        return ''.join(reversed(stra))





"""
核心思想，使用位运算，每4位，对应1位16进制数字。

使用0xf(00...01111b)获取num的低4位。
算数位移，其中正数右移左边补0，负数右移左边补1。

位移运算并不能保证num==0，需要使用32位int保证（对应16进制小于等于8位).


"""
#大神做法2
class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hex, ans = "0123456789abcdef",  ""
        while num and len(ans) < 8:
            ans = hex[num & 0xf] + ans
            num >>=  4
        return ans
