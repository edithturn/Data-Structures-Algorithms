class Queue:
	def __init__(self):
		self.queue = []
	def push(self, x):
		self.queue.append(x)
	def pop(self):
		self.queue.remove(self.queue[0])
	def top(self):
		return self.queue[0]
	def checkQueue(self):
		print (self.queue)

# Tests
my_queue = Queue()
my_queue.push(5)
my_queue.push(2)
my_queue.push(9)
my_queue.pop()
my_queue.checkQueue()