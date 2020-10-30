
"""给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。"""

#我的做法1
class Solution:
    def reverse(self, x: int) -> int:
        lis=str(x)
        lis=list(lis)
        if lis[0]=='-':
            lis1=lis[1:]
            lis1.reverse()
            lis1=list('-')+lis1
        else:
            lis1=lis[:]
            lis1.reverse()
        result =int( "".join(lis1))
        if -2**31<result<2**31-1:
            return result
        return 0



#我的做法2
class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        y=0
        if x<0:
            flag=1
        x=abs(x)
        while(x!=0):
            y=y*10+x%10
            x=int(x/10)
            if (-2 ** 31 < y < 2 ** 31 - 1) is False:
                return 0
        return 0-y if flag==1 else y
