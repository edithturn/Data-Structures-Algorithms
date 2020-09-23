COUNT = [10]

class newNode:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def print2DUtil (root, space):
	if (root == None):
		return
	
	space += (COUNT[0])

	print2DUtil(root.right, root.left)

	print()
	for i in range(COUNT[0], space):
		print(end = " ")
	print(root.data)

	print2DUtil(root.left, space)

def print2D(root):
	print2DUtil(root, 0)
	
if __name__ == '__main__':
	root = newNode(49)
	root.left = newNode(1)
	root.right = newNode(4)

	root.left.left = newNode(1)
	root.left.right = newNode(6)
	root.right.left = newNode(1)
	root.right.right = newNode(10)

	root.left.left.left = newNode(45)
	root.left.left.right = newNode(25)
	root.left.right.left = newNode(2)
	root.left.right.right = newNode(6)
	root.right.left.left = newNode(1)
	root.right.left.right = newNode(7)
	root.right.right.left = newNode(1)
	root.right.right.left = newNode(7)

	print2D(root)