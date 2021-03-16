"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"


"""


"""
切片再翻转再合并
"""
#大神做法1
class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))


"""
先反转单词列表 再反转字符串

以字符串 “I love drag queen” 为例：

s.split(" ") 
将字符串分割成单词列表:
['I', 'love', 'drag', 'queen']

s.split(" ")[::-1] 
将单词列表反转:
['queen', 'drag', 'love', 'I']

" ".join(s.split(" ")[::-1]) 
将单词列表转换为字符串，以空格分隔:
"queen drag love I"

" ".join(s.split(" ")[::-1])[::-1] 
将字符串反转：
”I evol gard neeuq“

"""

#大神做法2
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split(" ")[::-1])[::-1]
