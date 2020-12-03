"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。
例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"



"""


"""
26进制转换，太尼玛离谱了，数字题。
举个例子，52除以26，一直除的话实际上是20，但是0没有对应的位子，所以拆成1 26，所以是AZ，后面借了前面一位
"""
#我的做法
class Solution:
  def convertToTitle(self, n: int) -> str:
      str=''
      if n<=26:
          return chr(65+n-1)
      while n!=0:
          n, rightnum = divmod(n, 26)
          print("rightnum----",rightnum)
          if rightnum==0:
            str='Z'+str
            n=n-1#借一位
          else:
            str=chr(65+rightnum-1)+str
      return str
#大神做法1

"""
先减一，再除（难以理解）
"""
class Solution:
  def convertToTitle(self, n: int) -> str:
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n -= 1
    if n < 26:
      return eng[n]
    return self.convertToTitle(n // 26) + eng[n % 26]




