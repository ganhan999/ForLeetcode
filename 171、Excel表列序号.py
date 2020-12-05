"""
给定一个Excel表格中的列名称，返回其相应的列序号。
例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701

"""


"""
26进制转10进制
"""
#我的做法
class Solution:
  def titleToNumber(self, s: str) -> int:
    ans = 0
    lens = len(s)
    for i, s in enumerate(s):
      print(lens-i-1)
      ans = ans +(ord(s)-ord('A')+1)*26**(lens-i-1)
    return ans


#大神做法1

"""
ans*26相当于每次都往左边平移一位，给最右边一个位置
"""
class Solution(object):
  def titleToNumber(self, s):
    ans = 0
    for x in s:
      ans *= 26
      ans += ord(x) - ord('A') + 1
    return ans




