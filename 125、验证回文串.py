"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false


"""


"""
把不是字母和数字的字符全部去掉，然后转大写，再比较反转和原来的字符串是否相等
"""
#我的做法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        li=list([val for val in s if val.isalnum()])#去掉除字母和数字以外的字符
        li="".join(li).upper()#转大写
        return li==li[::-1]


#大神做法

"""
正则表达式

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.strip().lower())
        return s == s[::-1]

