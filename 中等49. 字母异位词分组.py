"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。


"""

"""
直接构造哈希表（字典形式），排序后的字母当作键，原字母当成值
"""

#大神做法1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))#sorted("abc")   --->['a', 'b', 'c']
            mp[key].append(st)#如果是普通的字典，那么这里就会报错，如果是defaultdict，默认值就是一个空列表
        return list(mp.values())






"""
直接构造哈希表（字典形式），将计数的字母表当作键，原字母当成值
"""

#大神做法2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        return list(mp.values())


"""
直接构造哈希表（字典形式），将转换的质数乘积当作键，原字母当成值

任何一个大于1的自然数N，如果N不为质数，那么N可以唯一分解成有限个质数的乘积
"""

#大神做法3
class Solution:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            c=1
            counts = [0] * 26
            for cc in st:
                c *= Solution.prime[ord(cc)-97]
            mp[c].append(st)
        return list(mp.values())




#python中defaultdict用法详解
'''
当我使用普通的字典时，用法一般是dict={},添加元素的只需要dict[element] =value即，调用的时候也是如此，

print(dict[element]),但前提是element字典里，如果不在字典里就会报错。

这时defaultdict就能排上用场了，defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值。

作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0
'''