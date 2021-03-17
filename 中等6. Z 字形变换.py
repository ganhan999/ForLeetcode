"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING"行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例2:
输入: s = "LEETCODEISHIRING", numRows =4
输出:"LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""



"""
先创建一个二维数组，然后遍历字符串，然后对应的一个个加入数组中，这里的flag是用来改变下标变化趋势的。
"""
#我的做法1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)


#大神做法1

"""
这道题只是需要相应的字符串，不要求输出，明显难度降低了，
因为这个图像是有规律的，发现每一满列对于行元素到下一满列对应行的元素距离是固定的，
为k= (numRows-1)*2，我们便可以以此为基础进行定位，逐行添加字符拼接成字符串。
时间复杂度实际是遍历一趟字符串s为O（n），空间复杂度O（n）


"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ans=""
        n=len(s)
        for i in range(numRows):
            k=i
            while k<n:
                ans+=s[k]
                k+=2*(numRows-1)
                if i!=0 and i!=numRows-1 and k-2*i <n:
                    ans+=s[k-2*i]
        return ans
