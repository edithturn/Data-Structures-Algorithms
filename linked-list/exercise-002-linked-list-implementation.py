class Node:
	def __init__(self, dataval=None):
		self.val = dataval
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def add_node(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		my_list = self.head
		while(my_list.next):
			my_list = my_list.next
		my_list.next = new_node

	def print_list(self):
		_list = self.head
		while _list is not None:
			print (_list.val)
			_list = _list.next

# Test
# Creating the object to Linked List
my_list = LinkedList()

# Creating 03 nodes
m_node1 = Node(7)
m_node2 = Node(2)
m_node3 = Node(6)

# Asigning the head of the Linked List to the first node
my_list.head = m_node2
# Linked the second node to the first node
my_list.head.next = m_node1
# Linked the thrid node to the second node
m_node1.next = m_node3
# Printing the Linked List
my_list.print_list()
