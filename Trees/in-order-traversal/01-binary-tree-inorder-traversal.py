class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Way
class SolutionRecursively:
    def inorderTraversal(self, root):
        if not root:
            return []      
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# Iterative Way
class SolutionIterative:
    def inorderTraversal(self, root):
        current = root
        stack = []
        _list = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                _list.append(current.val)
                current = current.right
            else:
                break
                
        return _list


node = Node(1)
node.right = Node(2)
node.right.left = Node(3)

print(SolutionRecursively().inorderTraversal(node))
print(SolutionIterative().inorderTraversal(node))