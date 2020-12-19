'''
LeetCode:
716. Max Stack
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Example:
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]
'''

class MaxStack:
	def __init__(self):
		self.stack = []

	def push(self, x:int) -> None:
		self.stack.insert(0,x)

	def pop(self) -> int:
		return self.stack.pop(0)

	def top(self) -> int:
		return self.stack[0]

	def peekMax(self) -> int:
		return max(self.stack)

	def popMax(self) -> int:
		m = max(self.stack)
		self.stack.remove(m)
		return m

# Tests
obj = MaxStack()
obj.push(5)
param1 = obj.push(1)
param2 = obj.push(5)
param3 =  obj.top()
param4 =  obj.popMax()
param5 =  obj.top()
param6 =  obj.peekMax()
param7 =  obj.pop()
param8 = obj.top()
print(param1, param2, param3, param4, param5, param6, param7, param8)