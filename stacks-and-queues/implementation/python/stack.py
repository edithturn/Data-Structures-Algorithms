# Defining the class for stack
class Stack:
	# Define "items" as an empty initial value
	def __init__(self):
		self.items = []
	# Return all the values of items in the list
	def isEmpty(self):
		return self.items == []
	# Add an item on the top of the list
	def push(self, item):
		self.items.append(item)
	# remove an item from the top of the list
	def pop(self):
		return self.items.pop()
	# TODO
	def peek(self):
		return self.items[len(self.items) - 1]
	# Return the length of the items
	def size(self):
		return len(self.items)