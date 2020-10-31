"""判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。"""


#我的做法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=x
        y=0
        if x<0:
            return False
        while(x!=0):
            y=y*10+x%10
            x=int(x/10)
        return y==x1#精髓啊！

#大神做法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]#str(x)[::-1]是反转数