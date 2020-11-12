---
title: '28、实现 strStr()'
date: 2020-11-07 18:04:00
tags: [leetcode]
published: true
hideInList: false
feature: /post-images/28、 实现 strStr().jpg
isTop: false
---


# 题目

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出
needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

"""

# 本体思路



利用python中find函数便可以直接找到，子字符串的初始位置。




# #我的做法：

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lens=len(nums)
        i=0
        if lens==0:
            return 0
        while i<=lens-1:
            if val in nums:
                inde=nums.index(val)
                nums.pop(inde)
                print()
            else:
                i=i+1
        return len(nums)

```



"""

# 大神做法1：

双指针法：题意可以理解为直接修改前k个数，因此无需删除操作

"""

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)



#复现成功！
```



# 大神做法2：

利用切片思想，循环len(haystack) - len(needle) + 1次

"""

```python
class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


#复现成功！
```

"""



"""
下面是find函数的介绍





"""


