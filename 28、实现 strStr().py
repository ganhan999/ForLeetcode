"""
实现strStr()函数。

给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出
needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回-1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回 0 。这与C语言的strstr()以及 Java的indexOf()定义相符。

"""

"""
思路分析：
利用python中find函数便可以直接找到，子字符串的初始位置。
"""
#我的做法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)



#大神做法1

"""
利用切片思想，循环len(haystack) - len(needle) + 1次
"""


class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1



"""
下面是find函数的介绍

描述
Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

语法
find()方法语法：

str.find(str, beg=0, end=len(string))
参数
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。

返回值
如果包含子字符串返回开始的索引值，否则返回-1。

实例
以下实例展示了find()方法的实例：

str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

以上实例输出结果如下：

15
15
-1

>>>info = 'abca'
>>> print info.find('a')    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
0
>>> print info.find('a',1)  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
3
>>> print info.find('3')    # 查找不到返回-1
-1

"""