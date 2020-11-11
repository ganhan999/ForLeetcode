# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#
#         if " " in s:
#             if set(s)!={" "}:
#                 inde=s.rfind(" ")
#                 return len(s)-inde-1
#             else:
#                 return 0
#         else:
#             return len(s)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip(" ")
        if " " in s:
            if set(s)!={" "}:
                inde=s.rfind(" ")
                return len(s)-inde-1
            else:
                return 0
        else:
            return len(s)
a=Solution()
print(a.lengthOfLastWord("a c"))