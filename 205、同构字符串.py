"""
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，
相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 
示例 1:
输入：s = "egg", t = "add"
输出：true

示例 2：
输入：s = "foo", t = "bar"
输出：false

示例 3：
输入：s = "paper", t = "title"
输出：true


"""


"""
双哈希表比较法
先把两个哈希表写出来
然后比较值是不是一样的
"""
#大神做法1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True

        if s == "" or t == "":
            return False

        hashmap_s = {}
        hashmap_t = {}

        # 对s中的字符进行录入，值为各个字符出现的下标
        for i, n in zip(s, range(len(s))):
            if i not in hashmap_s:
                hashmap_s[i] = [n]
            else:
                hashmap_s[i].append(n)

        # 对t中的字符进行录入，值为各个字符出现的下标
        for i, n in zip(t, range(len(t))):
            if i not in hashmap_t:
                hashmap_t[i] = [n]
            else:
                hashmap_t[i].append(n)

        # 对比两个哈希表值是否相同
        for value in hashmap_s.values():
            if value not in hashmap_t.values():
                return False

        return True




"""
双哈希表
互相映射
"""
#大神做法2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a2b, b2a = {}, {}
        n = len(s)
        for i in range(n):
            a, b = s[i], t[i]
            if (a in a2b and a2b[a] != b) or (b in b2a and b2a[b] != a):#是否互相映射
                return False
            a2b[a] = b
            b2a[b] = a
        return True