"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom
能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

 

示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true



"""

"""
首先利用collections.Counter 得到元素的计数集合
再利用差集
"""
#大神做法1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table_m = collections.Counter(magazine)
        hash_table_r = collections.Counter(ransomNote)

        """for i in hash_table_r:
            if hash_table_r[i] > hash_table_m[i]:
                return False
        return True"""
        return not hash_table_r - hash_table_m




"""
得到ransomnote的计数集合，然后分析magazine中的元素计数是不是比ransomnote的计数集合的更少
"""
#大神做法2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = dict(collections.Counter(ransomNote))
        for k, v in a.items():
            if magazine.count(k) < v:
                return False
        return True


