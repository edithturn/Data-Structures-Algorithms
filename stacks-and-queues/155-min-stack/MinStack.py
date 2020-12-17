'''
LeetCode:
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
'''
class MinStack:
	def __init__(self):
		self.stack = []
		self.min = []
	def push(self, x):
		if self.min_size == 0 or x <= self.min[-1]:
			self.min.append(x)
		self.stack.append(x)
	def pop(self):
		if (self.stack[-1] == self.min[-1]):
				self.min.pop()
		self.stack.pop()
	def top(self):
		return self.stack[-1]
	def getMin(self):
		return self.min[-1]

