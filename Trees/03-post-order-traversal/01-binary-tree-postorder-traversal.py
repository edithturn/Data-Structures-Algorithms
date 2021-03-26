class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Way
class SolutionRecursively:
    def postorderTraversal(self, root: Node):
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# Iterative Way
class SolutionIterative:
    def postorderTraversal(self, root: None):
        if root is None:
            return []

        stack = [root]
        _list = []
        while stack:
            root = stack.pop()
            _list.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return _list[::-1]



node = Node(1)
node.right = Node(2)
node.right.left = Node(3)

#  1
#   \   
#    2
#   /
#  3

print(SolutionRecursively().postorderTraversal(node))
print(SolutionIterative().postorderTraversal(node))