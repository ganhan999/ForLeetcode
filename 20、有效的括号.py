"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""

"""
思路分析：
这个题显然就要用到栈的知识，如果输入的是一个右边括号，如果他与栈顶的元素不对应时，则返回False，如果对应则弹出，
直到操作结束，判断栈是否为空。
"""
#我的做法
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


#大神做法

"""
对于正确的来说，每次都能去掉一对括号，最后就成了空
"""
class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''




"""
如何使列表最后一个元素弹出
1、pop方法
list = [1,2,3,4]
list.pop()
print(list)
 
#[1, 2, 3]

2、del方法
list = [1,2,3,4]
del(list[-1])
print(list)
 
# [1, 2, 3]

3、切片
list = [1,2,3,4]
list = list[0:-1]
print(list)

# [1,2,3]

总结：
以上三种方法未在内存处理上进行测试，唯一区别，pop方法和del方法如果对空列表进行操作，
会报错中断执行，切片方法不会因此报错，继续保持空列表向下运行
"""
