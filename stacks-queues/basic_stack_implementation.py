class Stack:
	def	__init__(self):
		self.stack = []
	def push(self, x):
		self.stack.append(x)
	def pop(self):
		self.stack.remove(self.stack[-1])
	def top(self):
		return self.stack[-1]
	def print(self):
		print(self.stack)

# Tests
my_stack = Stack()
my_stack.push(5)
my_stack.push(2)
my_stack.push(9)
my_stack.pop()
my_stack.print()

