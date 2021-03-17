"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。


注意：
你只能使用队列的基本操作 —— 也就是push to back、peek/pop from front、size 和is empty这些操作。
你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列,
只要是标准的队列操作即可。


示例：
输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False



"""


"""
单列表
"""
#大神做法1
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        q_length = len(self.q)
        while q_length > 1:
            self.q.append(self.q.pop(0)) #反转前n-1个元素，栈顶元素始终保留在队首
            q_length -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.q)



"""
双队列
"""

#大神做法2
from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.help = deque()
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
    def pop(self) -> int:#两个队列互相交换
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help,self.data = self.data,self.help
        return tmp
    def top(self) -> int:#同上 但是这里把顶元素加上了
        """
        Get the top element.
        """
        while len(self.data) != 1:#得到顶元素
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help.append(tmp)#加上顶元素
        self.help,self.data = self.data,self.help
        return tmp
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.data)

