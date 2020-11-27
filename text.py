from typing import List
from collections import deque
# import math
import re



class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        li=list([val for val in s if val.isalnum()])#去掉除字母和数字以外的字符
        li="".join(li).upper()#转大写
        return li==li[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

