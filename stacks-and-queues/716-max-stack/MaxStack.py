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
		self.max = []

	def push(self, x:int) -> None:
		if (len(self.stack) == 0 or x >= self.max[-1]):
			self.max.append(x)
		self.stack.append(x)

	def pop(self) -> int:
		return self.stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def peekMax(self) -> int:
		return self.max[-1]

	def popMax(self) -> int:
		while (self.stack[-1] != self.max[-1]):
			self.stack.pop()
		self.stack.pop()
		return self.max.pop()