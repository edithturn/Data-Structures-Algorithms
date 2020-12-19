class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.s1 = []
		self.s2 = []

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		while self.s1:
			self.s2.append(self.s1.pop())
		m = self.s1.append(x)
		while self.s2:
			self.s1.append(self.s2.pop())
		return m
	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		return self.s1.pop()

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		return self.s1[-1]

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		return not self.s1

# Testing
#["MyQueue","push","push","peek","pop","empty"]
#[[],[1],[2],[],[],[]]
#Answer:
#[null,null,null,1,1,false]

obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())
