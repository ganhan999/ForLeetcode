"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。


示例:
输入: "Hello World"
输出: 5




"""

"""
思路分析：
我工作效率低的原因完全是因为有和力扣的题干一样语文为负分的产品经理
由于有这种情况发生输入:"a "，输出:1
我们先要把左右测的空格去掉。然后利用rfind函数找到最后一个""在哪就行了。
"""
#我的做法
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(" ")
        if " " in s:
            if set(s)!={" "}:
                inde=s.rfind(" ")
                return len(s)-inde-1
            else:
                return 0
        else:
            return len(s)
#大神做法1

"""
为了解决最后一个字符串后面还有空格，倒序查找就行，当没有字符 (len = 0) 
时候，遇到空格就直接跳过。从有字符开始，每次不是空格就加 11，此时 len > 0
再次遇到空格，直接 return就是结果。要注意原字符串为全都是空格组成的字符串的情况，
也就是倒序扫描到字符串的开头依旧没更新 len，因此在循环外还需要 return 这种情况
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1, -1, -1):
            if length == 0 and s[i] == " ":
                continue
            if length != 0 and s[i] == " ":
                return length
            if s[i] != " ":
                length += 1
        return length


