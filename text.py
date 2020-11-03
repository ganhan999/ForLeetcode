class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(',']':'[','}':'{'}
        stack=[]
        for ele in s:
            if stack and ele in dic:
                if dic[ele]==stack[-1]:
                    stack.pop()
                else:return False
            else:
                stack.append(ele)
        return not stack
a=Solution()
print(a.isValid("()[]{}"))