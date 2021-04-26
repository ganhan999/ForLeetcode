"""
给定一个非空字符串   s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。



"""


""" 
相等则缩小指针继续遍历
不等则判断不包括字符s[r]的s[l : r]或者不包括字符s[l]的s[l + 1 : r + 1]是否为回文串即可
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #验证回文串函数
        def pending_str(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            #相等则缩小指针继续遍历
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                #不等则判断s[l : r]或者s[l + 1 : r + 1]是否为回文串即可
                if pending_str(s[l : r]) or pending_str(s[l + 1 : r + 1]):
                    return True
                else:
                    return False
        return True
