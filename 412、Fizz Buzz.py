"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果n是3的倍数，输出“Fizz”；

2. 如果n是5的倍数，输出“Buzz”；

3.如果n同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]



"""


"""
初始化一个空的答案列表。
遍历 1 ... N1...N。
对于每个数，判断它能不能同时被 3 和 5 整除，如果可以就把 FizzBuzz 加入答案列表。
如果不行，判断它能不能被 3 整除，如果可以，把 Fizz 加入答案列表。
如果还是不行，判断它能不能被 5 整除，如果可以，把 Buzz 加入答案列表。
如果以上都不行，把这个数加入答案列表。
"""
#大神做法1
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:ans.append('FizzBuzz')
            elif i%3==0:ans.append('Fizz')
            elif i%5==0:ans.append('Buzz')
            else:ans.append(str(i))
        return ans


