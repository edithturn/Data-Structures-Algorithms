class Node:
	def __init__(self, dataval=None):
		self.val = dataval
		self.next = None

class _LinkedList:
	def __init__(self):
		self.headval = None
	def _AddNewNode(self, data):
		new_node = Node(data)
		if self.headval is None:
			self.headval = new_node
			return
		ls = self.headval
		while(ls.next):
			ls = ls.next
		ls.next = new_node
	def _PrintNode(self):
		print_val = self.headval
		while print_val is not None:
			print (print_val.val)
			print_val = print_val.next

_list = _LinkedList()
_list.headval = Node("Monday")
s1 = Node("Tue")
s2 = Node("Wed")

_list.headval.next = s1
s1.next = s2

_list._AddNewNode("Thu")
_list._PrintNode()