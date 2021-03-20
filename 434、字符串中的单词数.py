"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

"""


"""
内置算法
"""
#大神做法1
class Solution:
    def countSegments(self, s):
        return len(s.split())

"""
计算单词的数量，就等同于计数单词开始的下标个数。因此，只需要定义好下标的条件，
就可以遍历整个字符串，检测每个下标。定义如下：若该下标前为空格（或者为初始下标），
且自身不为空格，则其为单词开始的下标。该条件可以以常数时间检测。最后，返回满足条件的下标个数。
相当于数空格的数量


"""
#大神做法2
class Solution:
    def countSegments(self, s):
        segment_count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1
        return segment_count



