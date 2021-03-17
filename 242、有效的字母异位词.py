"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false



"""


"""
哈希表

用哈希表统计第一个字符串中的字符数量；
再统计第二个字符串时，若字符在哈希表中，计数减一，否则返回false
最后判断哈希表中值是否都为0。
"""
#大神做法1
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True



"""
排序 然后逐位比较
"""

#大神做法2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ###用传统循环方法进行排序比较
        if len(s) != len(t):
            return False
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                return False
        return True



