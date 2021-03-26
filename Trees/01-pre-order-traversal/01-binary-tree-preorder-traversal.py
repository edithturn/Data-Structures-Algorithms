# Definition for a binary tree node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Way
class SolutionRecursively:
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# Iterative Way

class SolutionIterative:
    def preorderTraversal(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return result


node = Node(1)
node.right =  Node(2)
node.left =  None
node.right.left = Node(3)

#  1
#   \   
#    2
#   /
#  3

print(SolutionRecursively().preorderTraversal(node))
print(SolutionIterative().preorderTraversal(node))


# Morris traversal