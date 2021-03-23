# Definition for a binary tree node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

node = Node(1)
node.right =  Node(2)
node.right.left = Node(3)

print(Solution().preorderTraversal(node))