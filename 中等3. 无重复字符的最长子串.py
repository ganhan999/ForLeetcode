"""
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807


"""

"""
遍历每一个元素，选出最长子串。
"""
#我的做法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


#大神做法1

"""
用一个暂时存储匹配的子串来判断子串大小，如果出现重复的字符，找到重复的字符然后向后匹配。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用一个辅助变量来暂时存储匹配的子串
        ans = ''
        tep = ''
        for i in s:
            # 遍历，若不重复则记录该字符
            if i not in tep:
                tep += i
            # 如果遇到了已经存在的字符，则找到该字符所在位置，删除该字符，并保留该位置之后的子串，并把当前字符加入到最后，完成更新
            else:
                tep = tep[tep.index(i)+1:]
                tep += i
            # 如果是当前最长的，就替换掉之前存储的最长子串
            if len(tep) > len(ans):
                    ans = tep
        return len(ans)

#大神做法2

"""
动态规划

根据例子的思路推广至一般的情况：
给出一个字符串Si，已知它的最长子串长度为Li，如果在Si的末尾追加一个字符C，
即Si+1=Si+C，那么Si+1的最长子串是多少？
很容易想到：
lengthOfLongestSubString(Si+1)=max(Li,len(C结尾的无重复子串))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        return length
