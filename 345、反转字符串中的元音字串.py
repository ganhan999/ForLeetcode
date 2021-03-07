"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

 
示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"





"""


"""
双指针 
一个指向前面 一个指向后面
想找到前面的 然后找到后面的 然后交换顺序 继续找
直到两个指针相遇
"""
#大神做法1
class Solution:
    def reverseVowels(self, s: str) -> str:
        N = len(s)
        lst = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, N-1
        while i < j:
            if lst[i] in vowels:
                while i < j:
                    if lst[j] in vowels:
                        lst[i], lst[j] = lst[j], lst[i]
                        i += 1
                        j -= 1
                        break
                    else:
                        j -= 1
            else:
                i += 1
        return ''.join(lst)
