class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class ValidBST(object):
    def helperIsValidBST(self, node, low, high):
        if not node:
            return True
        val =  node.val
        if ((val > low and val < high) and
            self.helperIsValidBST(node.left, low, node.val) and 
            self.helperIsValidBST(node.right, node.val, high)):
            return True
        else:
            return False
    def isValidBST(self, node):
        return self.helperIsValidBST(node, float('-inf'), float('inf'))

node = Node(3)
node.left = Node(2)
node.right = Node(6)
node.right.left = Node(5)
node.right.right = Node(10)
#     3
#    / \
#   2   6
#      / \
#     5   10
print (ValidBST().isValidBST(node))


node1 = Node(3)
node1.left = Node(2)
node1.right = Node(6)
node1.right.left = Node(7)
node1.right.right = Node(10)
#     3
#    / \
#   2   6
#      / \
#    |7|   10 
print(ValidBST().isValidBST(node1))

node = Node(3)
node.left = Node(2)
node.right = Node(6)