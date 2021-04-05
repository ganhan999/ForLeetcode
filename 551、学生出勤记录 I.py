"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:
输入: "PPALLP"
输出: True

示例 2:
输入: "PPALLL"
输出: False


"""


"""
解决这个问题最简单的方法就是统计字符串中 A 的数目并检查 LLL
是否是给定字符串的一个子串。如果 AA 的数目比 22 少且 LLL 不是给定字符串的一个子串，那么返回 true，否则返回 false。


"""
#大神做法1
class Solution:
    def checkRecord(self, s: str) -> bool:
        #判断是否存在超过两个连续的'L'
        def pending_s(s):
            count = 0
            for i in range(0, len(s)):
                if s[i] == "L":
                    count += 1
                    if count > 2:
                        return False
                else:
                    count = 0
            return True
        #不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到)
        return s.count("A") <= 1 and pending_s(s)





