"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
。
"""

"""首先样例可能有
1、"a","b" 
2、"a",""
3、"ab","a"
4、"abbba","abbba"
5、""
这几种特殊情况，首先分析，如果空列表，就直接输出“”,例如栗子5。
其次如果出现栗子2这种情况，那么就要算出最小值如果是0，那么输出“”。
思路分析：
先算出最大可能前缀为a( (min(strs, key=lambda i: len(i)))) ，然后遍历所有列表的元素ele，进行比较。
注意如果出现了栗子4，那么就需要在最后return  strs[0][:i+1]。
其他情况下return strs[0][:i]，因为比较完的下一个不是相同前缀。
以后一定要记得先举例子分析！！！！
"""
#我的做法（超级傻逼，遇到了很多困难）
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs :
            return ''
        a = (min(strs, key=lambda i: len(i)))
        n = len(a)
        if n==0 :
            return a
        for i in range(n):
            c=strs[0][i]
            for ele in strs:
                if ele[i]==c:
                    continue
                else:
                        break
            else:
                continue
            return strs[0][:i]
        return  strs[0][:i+1]


#大神做法

"""
python两种让你拍大腿的解法，时间复杂度你想象不到，短小精悍。 
1、利用python的max()和min()，在Python里字符串是可以比较的，
按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
所以只需要比较最大最小的公共前缀就是整个数组的公共前缀(太妙了！！！）

2、利用python的zip函数，把str看成list然后把输入看成二维数组，
左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素
长度大于1之前的就是公共前缀（天才，灵活运用函数！）
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        s1 = min(strs)#利用ASCII码，最大和最小的比就行了。天才！
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        ss = list(map(set, zip(*strs)))#这里zip(*strs)是一个迭代器，如果list出来则是
                        # [('a', 'a', 'a'), ('b', 'b', 'b'), ('b', 'a', 'c'), ('a', 'a', 'a')]
                        #相当于二维数组左对齐，然后用set map一下，就变成”a“，”b“，”b，a，c“，”a“。然后算出长度就行了。
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res



"""
下面是zip函数的介绍
    >> > a = [1, 2, 3]
    >> > b = [4, 5, 6]
    >> > c = [4, 5, 6, 7, 8]
    >> > zipped = zip(a, b)  # 打包为元组的列表
    [(1, 4), (2, 5), (3, 6)]
    >> > zip(a, c)  # 元素个数与最短的列表一致
    [(1, 4), (2, 5), (3, 6)]
    >> > zip(*zipped)  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    [(1, 2, 3), (4, 5, 6)]
"""



"""
下面是 enumerate函数介绍
    >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))       # 下标从 1 开始
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]



    >>>i = 0
    >>> seq = ['one', 'two', 'three']
    >>> for element in seq:
    ...     print i, seq[i]
    ...     i +=1
    ... 
    0 one
    1 two
    2 three
    
    
    
    >>>seq = ['one', 'two', 'three']
    >>> for i, element in enumerate(seq):
    ...     print i, element
    ... 
    0 one
    1 two
    2 three
"""