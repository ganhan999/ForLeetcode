from typing import List
from collections import deque
# import math
import codecs

class Solution:
    def myAtoi(self, s: str) -> int:
        state=1
        flag=0
        s1=""
        for i in s:
            if flag==0:
                if i=="-":
                    s1+=i
                    flag=1
                elif i=="+":
                    s1 += i
                    flag=1
                elif i.isnumeric():
                    s1 += i
                    flag=1
                elif i.isspace():
                    continue
                else:
                    return 0
            else:
                if i.isnumeric():
                    s1 += i
                else:
                    break
        if s1[0]=="-":
            state=0
            s1=s1[1:]
        elif s1[0] == "+":
            s1=s1[1:]
        s1 =int(s1)
        if state==0:
            s1=-s1
        if s1>-2 ** 31 and s1<(2 ** 31) - 1:
            return s1
        elif s1<-2 ** 31:
            return  -2 ** 31
        else:
            return  (2 ** 31) - 1





print(Solution().myAtoi("+1"))