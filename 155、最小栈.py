"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop()—— 删除栈顶的元素。
top()—— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。


示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.



"""


"""
利用列表，生成栈
"""
#我的做法
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop()


    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
#大神做法1

"""
算法流程：

push()方法： 每当push()新值进来时，如果 小于等于 min_stack栈顶值，
则一起push()到min_stack，即更新了栈顶最小值；

pop()方法： 判断将pop()出去的元素值是否是min_stack栈顶元素值（即最小值），
如果是则将min_stack栈顶元素一起pop()，这样可以保证min_stack栈顶元素始终是stack中的最小值。

getMin()方法： 返回min_stack栈顶即可。

min_stack作用分析：
min_stack等价于遍历stack所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈。
相当于给stack中的降序元素做了标记，每当pop()这些降序元素，min_stack会将相应的栈顶元素
pop()出去，保证其栈顶元素始终是stack中的最小元素。


"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]




