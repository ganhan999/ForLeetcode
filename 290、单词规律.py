"""
给定一种规律 pattern和一个字符串str，判断 str 是否遵循相同的规律。
这里的遵循指完全匹配，例如，pattern里的每个字母和字符串str中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false



"""


"""
利用哈希表，用pattern中的元素为key，str中的单词为值，首先判断pattern中的元素有没有出现过，
如果出现过，那么判断对应的str的单词是不是不存在或着已经与别的单词配对
如果没出现过，那么就加到哈希表中


"""
#大神做法1
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        if len(s)!= len(pattern):
            return False
        dic = {}
        for i,x in enumerate(s):
            if pattern[i] not in dic:
                if x in dic.values():
                    return False
                dic[pattern[i]] = x
            else:
                if x != dic[pattern[i]]:
                    return False
        return True
