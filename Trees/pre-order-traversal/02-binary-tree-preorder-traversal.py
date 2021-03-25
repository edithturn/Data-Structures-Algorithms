class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Way
class SolutionRecursively:
    def inorderTraversal(self, root: Node):
        if not root:
            return []      
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# Iterative Way
class SolutionIterative:
    def inorderTraversal(self, root: Node):
        return 1
node = Node(1)
node.right = Node(2)
node.right.left = Node(3)

print(SolutionRecursively().inorderTraversal(node))