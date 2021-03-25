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
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            root = stack.pop
            if root.left is not None:
                stack.append(root.left)
                if root is not None:
                    result.append(root.val)
                if root.right is not None:
                    stack.append(root)
            return result



node = Node(1)
node.right = Node(2)
node.right.left = Node(3)
print(SolutionRecursively().inorderTraversal(node))

node1 = Node(1)
node1.right = Node(2)
node1.right.left = Node(3)
print(SolutionRecursively().inorderTraversal(node1))