"""
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多
相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。
要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

示例 1：
输入：n = 1
输出："1"
解释：这是一个基本样例。

示例 2：
输入：n = 4
输出："1211"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"

"""

"""
思路分析：
利用递归的思想，如果当后一个元素不等于前一个元素停止计数，以此类推。主要是递归的思想要掌握！
"""
#我的做法
class Solution:
    def countAndSay(self, n: int) -> str:
        if n<=1:
            return "1"
        pre=self.countAndSay(n-1)#递归的思想，要把递归写在一系列操作前面，最后写return
        res=""#从零开始
        count=1
        #以下条件是只有n>1才会发生的
        for i in range(len(pre)):
            if i==0:
                count=1
            elif pre[i]!=pre[i-1]:
                tmp=str(count)+pre[i-1]#如果当后一个元素不等于前一个元素停止计数，以此类推。
                res += tmp
                count=1
            elif  pre[i]==pre[i-1]:
                count=count+1
            if i==len(pre)-1:#为什么这里是if而不是elif，因为最后一个字符的时候也有可能满足上一个if。
                            #这里是为了如果是最后一个字符的时候就可以直接截断了
                tmp = str(count) + pre[i]
                res += tmp
        return res


#大神做法1

"""
双指针探测
https://leetcode-cn.com/problems/count-and-say/solution/
38-wai-guan-shu-lie-shuang-zhi-zhen-by-yiluolion/
如图所示
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        pre = ''
        cur = '1'#默认为“1”
        # 从第 2 项开始
        for _ in range(1, n):
            # 这里注意要将 cur 赋值给 pre
            # 因为当前项，就是下一项的前一项。有点绕，尝试理解下
            pre = cur
            # 这里 cur 初始化为空，重新拼接
            cur = ''
            # 定义双指针 start，end
            start = 0
            end = 0
            # 开始遍历前一项，开始描述
            while end < len(pre):
                # 统计重复元素的次数，出现不同元素时，停止
                # 记录出现的次数，
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # 元素出现次数与元素进行拼接
                cur += str(end - start) + pre[start]
                # 这里更新 start，开始记录下一个元素
                start = end
        return cur





#大神做法2

"""
递归和迭代简单算法
"""

def countAndSay(self, n: int) -> str:
    if n == 1:
        return '1'
    s = self.countAndSay(n - 1)

    i, res = 0, ''
    for j, c in enumerate(s):
        if c != s[i]:
            res += str(j - i) + s[i]#后面使用 j - i 来统计相同元素的个数，这样最后会剩下最后一堆相同的数字。
            i = j
    res += str(len(s) - i) + s[-1]  # 所以最后一个元素莫忘统计
    return res


def countAndSay(self, n: int) -> str:
    res = '1'#默认为“1”
    for _ in range(n-1):  # 控制循环次数
        i, tmp = 0, ''
        for j, c in enumerate(res):
            if c != res[i]:
                tmp += str(j-i) + res[i]
                i = j
        res = tmp + str(len(res) - i) + res[-1]
    return res

"""
Python递归的要点
1、一定要画图
2、在最前面写上递归停止的条件
3、在递归函数后面要写上你相对应的操作，并在最后写上return

Python迭代的要点
1、利用while循环将递归变为非递归



递归和迭代的区别：

斐波那契数列的实现

【递归实现】

def fib(x):
    if x <2:
        return 0 if x==0 else 1
    else:
        return fib(x - 1) + fib(x - 2)
 
print(fib(6))


【迭代实现】

def fib(x):
    n1 = 1
    n2 = 1
    n3 = 1
 
    while x-2 > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        x -= 1
    return n3
 
num = int(input('请输入一个正整数：'))
print(fib(num))
"""