"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

"""


"""
如果s中包含重复的子字符串，那么说明s中至少包含两个子字符串，s+s至少包含4个字串，前后各去掉一位，查找s是否在新构建的字符串中。
"""
#大神做法1
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]





"""
把两个字符串s拼接在一起，会有以下两种情况：

当s不是循环字符串时：
第一次发现s的起点是在lens（s）

当s是循环字符串时：
第一次发现s的起点是在小于lens（s）
"""
#大神做法1
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).find(s,1) != len(s)

